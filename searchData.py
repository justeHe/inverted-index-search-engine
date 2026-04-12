import os
import json
import ujson
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from text_processing import process
from tfidf_model import build_tfidf

tfidf = TfidfVectorizer()

pub_name = []
pub_url = []
pub_author = []

with open('scraper_results.json', 'r') as f:    doc = f.read()
scraper_result = ujson.loads(doc)

for item in scraper_result:
    pub_name.append(item['name'])
    pub_url.append(item['link'])
    pub_author.append(item['author'])

with open('publication_list_stemmed.json', 'r') as f:   doc = f.read()
pub_list_stemmed = ujson.loads(doc)
tfidf, tfidf_matrix = build_tfidf(pub_list_stemmed)

with open('publication_indexed_dictionary.json', 'r') as f: doc = f.read()
data_dict = ujson.loads(doc)


collective_output = {}


def search_data(query):
    query_tokens = process(query)
    query_str = " ".join(query_tokens)

    query_vec = tfidf.transform([query_str])
    cosine_output = cosine_similarity(tfidf_matrix, query_vec)

    scores = []
    for i, score in enumerate(cosine_output):
        scores.append((i, float(score[0])))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    results = []

    for doc_id, score in scores[:10]:
        if score > 0:
            results.append({
                "name": pub_name[doc_id],
                "url": pub_url[doc_id],
                "author": pub_author[doc_id],
                "score": round(score, 4)
            })

    return results


search_data("art")
