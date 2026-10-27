from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

app = FastAPI(title="Articles API")

@app.get("/articles")
def get_articles(db: Session = Depends(get_db)):
    try:
        query = text("SELECT ID, Topic, SiteURL, Author, Title, Header, Text FROM articlescrapper")
        result = db.execute(query).mappings().all()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/articles/{article_id}")
def get_article(article_id: int, db: Session = Depends(get_db)):
    try:
        query = text("SELECT ID, Topic, SiteURL, Author, Title, Header, Text FROM articlescrapper WHERE ID = :id")
        result = db.execute(query, {"id": article_id}).mappings().first()
        
        if not result:
            raise HTTPException(status_code=404, detail="Nie znaleziono")
            
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))