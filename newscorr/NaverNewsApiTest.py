import os
import sys
import urllib.request
import requests
from newspaper import Article
import json
import pandas as pd
import numpy as np
import glob
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from gensim.models.word2vec import Word2Vec
import networkx as nx
import matplotlib.pyplot as plt

def printcorr(path):
    #pos_review = glob.glob(path)[0:100]
    pos_lines = []
    for i in os.listdir(path):
        print(i)
        try:
            f = open(path+"/"+i, "r")
            temp = f.readlines()[0]
            pos_lines.append(temp)
            f.close()
        except Exception as e:
            continue
    print(len(pos_lines))
    # 단어 추출하기
    #stop_words = stopwords.words("korean")
    tokenizer = RegexpTokenizer("[\w]+")
    text = []
    for line in pos_lines:
        words = line.lower()
        tokens = tokenizer.tokenize(words)
        #stopped_tokens = [i for i in list(set(tokens)) if not i in stop_words + ["br"]]
        #stopped_tokens2 = [i for i in stopped_tokens if len(i) > 1]
        text.append(tokens)

    print(text)
    # word2vec 기반의 연관어 분석
    model = Word2Vec(text, sg = 1, window = 2, min_count = 3, epochs=100)
    model.init_sims(replace = True)
    #model.wv.similarity("film", "movie")
    print(str(model.wv.most_similar("삼성전자", topn = 10)))
    #print(str(model.wv))
    return model

m = printcorr("news")
top10 = m.wv.most_similar("삼성전자",topn=10)
edge = []
for x in top10:
    edge += [("삼성전자",x[0])]
print(str(edge))
m.wv.save("result.txt")
G = nx.Graph()
G.add_edges_from(edge)
nsize = []
i = 0
for n in nx.nodes(G):
    if(n == "삼성전자"):
        nsize.append(20**2)
        continue
    nsize.append((top10[i][1]**2 * 20)**2)
    i+=1

        


pos = {}
for n in nx.nodes(G):
   if(n == "삼성전자"):
       pos[n] = [0,0]
       continue
   pos[n] = [np.random.randint(-80,80)/10,np.random.randint(-60,60)/10]

plt.figure(figsize=(16,12))
plt.axis("off")

nx.draw_networkx(G,pos,node_size=nsize,font_family="gulim")
#nx.draw_networkx(G,pos,font_family="gulim")

plt.show()
while(True):
    a=0




client_id = "byQ5h8cDSAXKBbwgxAHq"
client_secret = "2xPxQwfaJc"
data = {
    'query':"삼성전자", # 검색어
    'display':100, # 검색 개수 default : 10, max : 100
    'start':1, # 검색 시작 위치 default : 1, max : 1000
    'sort':"sim" # 검색 결과 정렬 방법 : sim 정확도순, date 날짜순
}
data = urllib.parse.urlencode(data)
headers = {
    "X-Naver-Client-Id":client_id,
    "X-Naver-Client-Secret":client_secret
    }
result = requests.get("https://openapi.naver.com/v1/search/news.json?", headers=headers, params=data)

#response = urllib.request.urlopen(request)
rescode = result.json()
f = open("json.txt", 'w')
f.write(str(rescode))
f.close()
count = 0
print(len(rescode))
ls = rescode["items"]
def crawl_article_context(url):
    try:
        article = Article(url, language='ko')
        article.download()
        article.parse()
        if(article.title != None and article.text != None):
            return (article.title,article.text)
        return None
    except:
        return None


for i in ls:
    try:
        link = i["originallink"]
        text = crawl_article_context(link)
        if(text == None):
            continue
        path = "news/"+text[0]+".txt"
        f = open(path,"w")
        f.write(text[1])
        f.close()
        printcorr(path)
    except:
        continue
while(True):
    a=0
if(rescode==200):
    response_body = result.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)