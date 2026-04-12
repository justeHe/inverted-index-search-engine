from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf(docs):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(docs)
    return vectorizer, matrix