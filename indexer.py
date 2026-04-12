import os
import ujson
import json
import nltk
from text_processing import process


with open('scraper_results.json', 'r') as f:
    scraper_results = f.read()
data_dict = json.loads(scraper_results)

pub_name = []
pub_url = []
pub_author = []


for item in data_dict:
    pub_name.append(item['name'])
    pub_url.append(item['link'])
    pub_author.append(item['author'])



pub_list = []
pub_list_special_rm = []


data_dict = {}
pub_list_stemmed = []

for i in range(len(pub_name)):
    tokens = process(pub_name[i])
    pub_list_stemmed.append(" ".join(tokens))

    tf_count = {}
    for t in tokens:
        tf_count[t] = tf_count.get(t, 0) + 1

    for term, tf in tf_count.items():
        if term not in data_dict:
            data_dict[term] = []
        data_dict[term].append((i, tf))

with open('publication_list_stemmed.json', 'w') as f:
    json_str = ujson.dumps(pub_list_stemmed)
    f.write(json_str)


with open('publication_indexed_dictionary.json', 'w') as f:
    print(data_dict)
    json_str = ujson.dumps(data_dict)
    f.write(json_str)

