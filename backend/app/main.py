from typing import Union, Optional
from fastapi import FastAPI, Response, Request, Depends, Query, Header
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

import os
import json
import pandas as pd

from fastapi.logger import logger
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

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
DATAFRAME_PATH = os.path.join(DATA_DIR, 'all_news_with_sentiment.csv')
news_df = pd.read_csv(DATAFRAME_PATH)

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
    # logger.info(os.path.realpath(__file__))
    # return Response(result, media_type="application/json")
    return {"message": "Hello World"}
    # return {"hello goodbye"}

@app.post("/search")
async def request_search(search:dict) -> dict:
    logger.info("Hello!")
    logger.info(search)
    # return {'data': 'good'}
    return search

@app.get("/search/{search}&{start_date}&{end_date}")
async def request_search(search, start_date, end_date):
    logger.info(search)
    logger.info(start_date)
    logger.info(end_date)

    start_date = ''.join(start_date.split('-'))
    end_date = ''.join(end_date.split('-'))
    search_df = news_df[(news_df['search'] == search) & 
                        (news_df['news_date'] >= int(start_date)) & 
                        (news_df['news_date'] <= int(end_date))]
    search_df = search_df[['title', 'news_date']]
    search_dict = search_df.to_dict(orient='records')

    return {"data" : search_dict}
