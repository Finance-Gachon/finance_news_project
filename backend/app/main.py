from typing import Union, Optional
from fastapi import FastAPI, Response, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

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

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    result = json.dumps({"message": "Hello World"})
    # return Response(result, media_type="application/json")
    return {"message": "Hello World"}
    # return {"hello goodbye"}

@app.get("/news/", response_model=list[schemas.News_crwal])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_news(db)
    return news

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}