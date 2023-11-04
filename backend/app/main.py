from typing import Union
from fastapi import FastAPI, Response, Request, Depends
from fastapi.encoders import jsonable_encoder
import json
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
async def root():
    result = json.dumps({"message": "Hello World"})
    return Response(result, media_type="application/json")

@app.get("/news/", response_model=list[schemas.News_crwal])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_news(db)
    return news