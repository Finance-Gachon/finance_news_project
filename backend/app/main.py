from typing import Union, Optional
from fastapi import FastAPI, Response, Request, Depends, Query, Header
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

import os
import pandas as pd
from collections import Counter, defaultdict
import logging

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
NEWS_PATH = os.path.join(DATA_DIR, 'news_data.csv')
CORR_PATH = os.path.join(DATA_DIR, 'corr_news_data.csv')
STOP_WORDS_PATH = os.path.join(DATA_DIR, 'stop_words.txt')

news_df = pd.read_csv(NEWS_PATH)
corr_df = pd.read_csv(CORR_PATH)

f = open(STOP_WORDS_PATH, 'r', encoding='utf-8')
stop_words = f.readlines()
stop_words = [word.strip() for word in stop_words]
f.close()

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

    # news 불러오기
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

    # 검색어와 날짜에 해당하는 상관계수 불러오기
    partial_corr_df = corr_df[(corr_df['search'] == search) & 
                              (corr_df['news_date'] >= int(start_date)) & 
                              (corr_df['news_date'] <= int(end_date))]

    corr_dict = defaultdict(int)
    date_length = int(end_date) - int(start_date) + 1

    for word, corr in zip(partial_corr_df['word'], partial_corr_df['corr']):
        if word not in stop_words: 
            corr_dict[word] += corr / date_length
    
    word_and_corr = sorted(corr_dict.items(), key=lambda item: -item[1])
    max_value = word_and_corr[0][1]

    # 오로지 긍정과 부정의 비율 계산 (중립은 제외)
    p_n_df = search_df[search_df['label'] != 'neutral']
    p_n_label_df = p_n_df['label'].value_counts() / len(p_n_df)
    p_n_label_dict = p_n_label_df.to_dict()

    max_positive_date = 0
    max_negative_date = 0

    max_positive = 0
    max_negative = 0

    for news_date in p_n_df['news_date'].unique():
        tmp_df = p_n_df[p_n_df['news_date']==news_date]                
        tmp_df = tmp_df['label'].value_counts() / len(tmp_df)
        
        if max_positive < tmp_df['positive']:
            max_positive_date = news_date
            max_positive = tmp_df['positive']
        
        if max_negative < tmp_df['negative']:
            max_negative_date = news_date
            max_negative = tmp_df['negative']

    max_positive_date = str(max_positive_date)
    max_positive_date = max_positive_date[:4] + '.' + max_positive_date[4:6] + '.' + max_positive_date[6:]

    max_negative_date = str(max_negative_date)
    max_negative_date = max_negative_date[:4] + '.' + max_negative_date[4:6] + '.' + max_negative_date[6:]

    max_pos_neg_date = {'positive': max_positive_date, 'negative': max_negative_date}
    logger.info(max_pos_neg_date)

    word_and_corr = [(word, corr * 100 / max_value)for word, corr in word_and_corr][:10]
    return {"data" : search_dict,
            "sentiment": sentiment_result, 
            "similar": word_and_corr,
            "pos_neg": p_n_label_dict,
            "max_pos_neg": max_pos_neg_date}
