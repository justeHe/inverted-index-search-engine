```md
# 📚 Inverted Index Search Engine

## 🧠 Overview

This project is a simple Information Retrieval (IR) system built for course practice.  
It demonstrates the core pipeline of a search engine, including:

- Web scraping
- Text preprocessing
- Inverted index construction
- TF-IDF ranking
- Cosine similarity retrieval
- Web-based search interface (Flask)

---

## ⚙️ System Architecture

```

Crawler → Preprocessing → Inverted Index → TF-IDF Vectorization → Ranking → Web UI

```

---

## 📦 Features

### ✔ Web Scraping
- Extracts book information (title, author, link)
- Source: No Starch Press programming catalog

### ✔ Text Processing
- Tokenization (NLTK)
- Stopword removal
- Stemming (Porter Stemmer)
- Special character filtering

### ✔ Inverted Index
- Term → document mapping
- Supports term frequency (TF)

### ✔ Ranking Model
- TF-IDF vectorization (sklearn)
- Cosine similarity scoring

### ✔ Search Engine
- Multi-word query support
- Ranked retrieval results

### ✔ Web Interface
- Flask backend
- HTML-based search UI
- JSON API communication

---

## 📁 Project Structure

```

project/
│
├── scraper.py                          # Web crawler
├── indexer.py                         # Build inverted index
├── searchData.py                      # Search & ranking logic
│
├── text_processing.py                 # Shared preprocessing module
├── tfidf_model.py                     # TF-IDF model builder
│
├── web_app.py                         # Flask backend server
│
├── scraper_results.json              # Raw scraped data
├── publication_indexed_dictionary.json
├── publication_list_stemmed.json
│
├── templates/
│   └── index.html                    # Web UI

````

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

---

### 2. Download NLTK resources

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

### 3. Run the pipeline

```bash
python scraper.py
python indexer.py
python web_app.py
```

---

### 4. Open browser

```
http://127.0.0.1:5000
```

---

## 🔍 Example Queries

* machine learning
* python security
* deep learning
* data science
* information retrieval

---

## 📊 Techniques Used

* Inverted Index
* TF-IDF weighting
* Cosine similarity
* Text preprocessing pipeline
* Web scraping (BeautifulSoup)
* Flask web framework

---

## 🧪 Limitations

* No BM25 ranking model
* No query expansion
* No phrase search support
* Small dataset (single source website)
* Basic ranking strategy

---

## 🚀 Future Improvements

* BM25 ranking model
* Query suggestion (autocomplete)
* Phrase search (positional index)
* Elasticsearch integration
* Frontend framework upgrade (Vue/React)
* Relevance evaluation (Precision / Recall)

---

## 👨‍💻 Author

Course project for Information Retrieval system implementation.

```
```
