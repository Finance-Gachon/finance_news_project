from typing import Union, Optional
from fastapi import FastAPI, Response, Request, Depends, Query, Header
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

import json
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

from fastapi.logger import logger
# ... other imports
import logging

company_searching = [
    {
        "company_name": "삼성전자",
        "item": "Read a book."
    },
    {
        "company_name": "LG에너지솔루션",
        "item": "Read a book."
    }
]

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
logger = logging.getLogger("uvicorn.error")

origins = [
    "http://localhost:3000",
    "localhost:3000"
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
    search='삼성전자'
    logger.info(search)
    logger.info(msg="Hello!")
    # return Response(result, media_type="application/json")
    return {"message": "Hello World"}
    # return {"hello goodbye"}

@app.post("/search")
async def request_search(search:dict) -> dict:
    logger.info("Hello!")
    logger.info(search)
    # return {'data': 'good'}
    return search

@app.get("/search/{company_name}&{start_date}&{end_date}")
async def request_search(company_name, start_date, end_date):
    logger.info(company_name)
    logger.info(start_date)
    logger.info(end_date)
    
    new_companys = []
    for one in company_searching:
        if one["company_name"] == company_name:
            new_companys.append(one)

    return {"data" : new_companys}
