import mysql.connector
import requests
from bs4 import BeautifulSoup

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktyki"
)
cursor = db.cursor()

print("Connected:", db.is_connected())

sources = [
    {
        "name": "CoinDesk",
        "url": "https://www.coindesk.com/",
        "topic": "Crypto",
        "link_filter": "/2026/"  
    },
    {
        "name": "Finance",
        "url": "https://finance.yahoo.com/",
        "topic": "Stocks",
        "link_filter": "/news/"   
    }, 
    {
        "name": "US Financial Policy",
        "url": "https://www.cnbc.com/id/15839069",
        "topic": "US Financial Policy",
        "link_filter": "/2026/"
    },
    {
        "name": "Business",
        "url": "https://www.cnbc.com/business/",
        "topic": "Business",
        "link_filter": "/2026/"
    }
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def parse_article(url):
    """Fetches article page, author, title, headings, and text content."""
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            return None
            
        soup = BeautifulSoup(res.text, 'html.parser')
        
        article_container = (
            soup.find('article') or 
            soup.find('div', class_=lambda x: x and ('article' in x.lower() or 'content' in x.lower() or 'story' in x.lower())) or 
            soup
        )
        
        h1_tag = soup.find('h1')
        title = h1_tag.get_text().strip() if h1_tag else "No title"
        
        author = "Unknown author"
        author_meta = soup.find('meta', attrs={'name': 'author'}) or soup.find('a', rel='author')
        if author_meta:
            author = author_meta.get('content') or author_meta.get_text().strip()
        else:
            author_tag = soup.find(class_=lambda x: x and 'author' in x.lower())
            if author_tag:
                author = author_tag.get_text().strip()

        headings = [h.get_text().strip() for h in article_container.find_all(['h2', 'h3']) if len(h.get_text().strip()) > 3]
        
        paragraphs = article_container.find_all('p')
        content_list = [p.get_text().strip() for p in paragraphs if len(p.get_text().strip()) > 20]
        content = " ".join(content_list) if content_list else "No content found"
        
        return {
            "title": title,
            "author": author,
            "headings": headings,
            "content": content
        }
    except Exception as e:
        print(f"   [!] Error fetching article {url}: {e}")
        return None


for source in sources:
    source_name = source["name"]
    category_url = source["url"]
    topic = source["topic"]
    link_filter = source["link_filter"]
    
    print("\n" + "="*80)
    print(f"Categori: {topic}")
    print("="*80)

    try:
        response = requests.get(category_url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            continue
            
        soup = BeautifulSoup(response.text, 'html.parser')
        article_links = set()

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href'].strip()

            if href.startswith('/'):
                base_url = "/".join(category_url.split("/")[:3])
                href = base_url + href

            if link_filter in href and href.startswith("http"):
                if "/videos/" in href or href.endswith("/news/") or href.count('/') < 4:
                    continue
                article_links.add(href)

        for link in list(article_links)[:3]:
            article_data = parse_article(link)
            print()

            if article_data:
                print(f"URL:       {link}")
                print(f"AUTHOR:    {article_data['author']}")
                print(f"TITLE:     {article_data['title']}")
                headings_text = " | ".join(article_data['headings']) if article_data['headings'] else "No headings found"
                print(f"HEADINGS:  {headings_text}")
                print(f"TEXT:      {article_data['content'][:200]}...")
    except Exception as e:
        print(f"Connection error: {e}")

cursor.close()
db.close()