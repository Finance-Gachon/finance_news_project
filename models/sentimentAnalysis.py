from transformers import Pipeline, pipeline, AutoModelForSequenceClassification, AutoTokenizer
import torch
import pandas as pd
import os
import sys
from pathlib import Path
ASSETS_DIR_PATH = os.path.join(Path(__file__).parent, "")

tokenizer = AutoTokenizer.from_pretrained("snunlp/KR-FinBert-SC")
model = AutoModelForSequenceClassification.from_pretrained("snunlp/KR-FinBert-SC")
sentiment_model = pipeline(model="snunlp/KR-FinBert-SC")


if __name__ == "__main__":
    df = pd.read_csv("./삼성전자.csv")

    print(tokenizer(df['title'][0]))
    # print(df)

    # TODO: 여기서 나오는 score는 어떻게 계산되는지 확인할 것!
    
    print(sentiment_model([df['title'][0]]))
    
    print(sentiment_model(['삼성전자는 이날 50% 하락하였습니다.']))
    