# 📰 금융 뉴스

## 🗄 디렉토리 구조 <a name='folder'></a>
```Plain Text
├──📁assets
│   └── img
│
├──📁backend
│   └──📁app
│
├──📁crwal
│   └── NAVER api 크롤링
│
├──📁frontend
│
├──📁models
└──
```

<br><br>

## ⚙️ 설정 사항 <a name='setup'></a>

### 1. Conda Create
```bash
$ conda create -n bigdata python=3.
$ conda activate bigdata
```

### 2. Requirements

```bash
$ pip install -r requirements.txt
```
<br><br>
## 💻 실행하는 법 <a name='torun'></a>

### Train

```bash
$ python main.py -m t
$ python main.py -m train
```

### Inference

```bash
$ python main.py -m i
$ python main.py -m inference
```

### Hyper-parameter Searching
```bash
$ python main.py -m h
$ python main.py -m hp_searching
```

### Optuna Searching
```bash
$ python main.py -m o
$ python main.py -m optuna
```