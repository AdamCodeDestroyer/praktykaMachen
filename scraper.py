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
        "url": "https://www.coindesk.com/",
        "topic": "Crypto",
        "link_filter": "/news/"
    },
    {
        "url": "https://finance.yahoo.com/",
        "topic": "Stocks",
        "link_filter": "/news/"
    }, 
    {
        "url": "https://www.cnbc.com/id/15839069",
        "topic": "US Financial Policy",
        "link_filter": "/2026/"
    },
    {
        "url": "https://www.cnbc.com/business/",
        "topic": "Business",
        "link_filter": "/2026/"
    }
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

for source in sources:
    category_url = source["url"]
    topic = source["topic"]
    link_filter = source["link_filter"]
    print(f"\nScanning source: {category_url} [Topic: {topic}]")

    try:
        response = requests.get(category_url, headers=headers, timeout=10)
        print(f"HTTP Status: {response.status_code}")
        
        if response.status_code != 200:
            continue
            
        soup = BeautifulSoup(response.text, 'html.parser')
        article_links = set()
        
    except Exception as e:
        print(f"Błąd połączenia: {e}")

cursor.close()
db.close()
