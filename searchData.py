import ujson
from sklearn.metrics.pairwise import cosine_similarity
from text_processing import process
from tfidf_model import build_tfidf

ALPHA = 0.7

FIELD_WEIGHTS = {
    "title": 0.7,
    "author": 0.2,
    "summary": 0.1
}


# 加载数据
data = ujson.load(open('scraper_results.json', 'r', encoding='utf-8'))

title_docs = ujson.load(open('title_docs.json', 'r', encoding='utf-8'))
author_docs = ujson.load(open('author_docs.json', 'r', encoding='utf-8'))
summary_docs = ujson.load(open('summary_docs.json', 'r', encoding='utf-8'))

# TF-IDF
tfidf_title, mat_title = build_tfidf(title_docs)
tfidf_author, mat_author = build_tfidf(author_docs)
tfidf_summary, mat_summary = build_tfidf(summary_docs)

# 简单语义向量
tfidf_vector, mat_vector = build_tfidf(summary_docs)


def search_data(query):
    tokens = process(query)
    q = " ".join(tokens)

    # 各字段相似度
    q_title = tfidf_title.transform([q])
    q_author = tfidf_author.transform([q])
    q_summary = tfidf_summary.transform([q])

    sim_title = cosine_similarity(mat_title, q_title)
    sim_author = cosine_similarity(mat_author, q_author)
    sim_summary = cosine_similarity(mat_summary, q_summary)

    # 语义匹配
    q_vec = tfidf_vector.transform([q])
    sim_vector = cosine_similarity(mat_vector, q_vec)

    results = []

    for i in range(len(data)):

        #文本分
        S_text = (
            FIELD_WEIGHTS["title"] * sim_title[i][0] +
            FIELD_WEIGHTS["author"] * sim_author[i][0] +
            FIELD_WEIGHTS["summary"] * sim_summary[i][0]
        )

        #语义
        S_vector = sim_vector[i][0]

        #融合
        score = ALPHA * S_text + (1 - ALPHA) * S_vector

        results.append((i, score))

    # 排序
    results = sorted(results, key=lambda x: x[1], reverse=True)

    output = []
    for doc_id, score in results[:10]:
        if score > 0:
            output.append({
                "name": data[doc_id]["name"],
                "url": data[doc_id]["link"],
                "author": data[doc_id]["author"],
                "summary": data[doc_id].get("summary", "")[:150],
                "score": round(score, 4)
            })

    return output


if __name__ == "__main__":
    res = search_data("machine learning")
    for r in res:
        print(r)