import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

STOPWORDS = set(stopwords.words('english'))
stemmer = PorterStemmer()

def process(text):
    # 去非字母
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # 分词
    words = word_tokenize(text.lower())

    # 去停用词 + stemming
    result = []
    for w in words:
        if w not in STOPWORDS:
            result.append(stemmer.stem(w))

    return result