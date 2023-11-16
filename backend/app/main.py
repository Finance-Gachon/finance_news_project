from typing import Union, Optional
from fastapi import FastAPI, Response, Request, Depends, Query, Header
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

import os
import pandas as pd
from collections import Counter
import logging

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
    return {"message": "Hello World"}

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
    search_df = search_df[['title', 'news_date', 'label', 'URL']]
    search_df = search_df.dropna()
    search_dict = search_df.to_dict(orient='records')

    sentiment_result = []

    for one_date in search_df['news_date'].unique():
        tmp_df = search_df[search_df['news_date'] == one_date]
        row = Counter(tmp_df['label'])
        row = dict(row)
        one_date = str(one_date)
        one_date = one_date[:4] + '-' + one_date[4:6] + '-' + one_date[6:]
        row.update({"date":str(one_date)})
        sentiment_result.append(row)

    sentiment_result.reverse()

    return {"data" : search_dict,
            "sentiment": sentiment_result}
