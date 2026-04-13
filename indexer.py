import json
import ujson
from text_processing import process

with open('scraper_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

title_docs = []
author_docs = []
summary_docs = []

for item in data:
    title_docs.append(" ".join(process(item.get("name", ""))))
    author_docs.append(" ".join(process(item.get("author", ""))))
    summary_docs.append(" ".join(process(item.get("summary", ""))))

ujson.dump(title_docs, open('title_docs.json', 'w', encoding='utf-8'))
ujson.dump(author_docs, open('author_docs.json', 'w', encoding='utf-8'))
ujson.dump(summary_docs, open('summary_docs.json', 'w', encoding='utf-8'))

print("Index built (multi-field)")