# 📚 Inverted Index Search Engine

[](https://www.python.org/downloads/)
[](https://flask.palletsprojects.com/)
[](https://opensource.org/licenses/MIT)

A lightweight Information Retrieval (IR) system designed for educational purposes. This project demonstrates the full lifecycle of a search engine, from automated data collection to ranked document retrieval using vector space models.

-----

## 🏗️ System Architecture

The engine follows a standard linear pipeline:
`Web Scraper` → `Text Preprocessing` → `Inverted Indexing` → `TF-IDF Vectorization` → `Cosine Similarity Ranking` → `Flask Web UI`

-----

## 🌟 Key Features

### 🕷️ Automated Data Collection

  * **Targeted Crawling:** Extracts book metadata (Titles, Authors, URLs) from the No Starch Press programming catalog.
  * **Persistent Storage:** Saves raw data in structured JSON format for offline processing.

### 🧠 Advanced NLP Pipeline

  * **Tokenization:** Breaks down raw text using NLTK’s `punkt` tokenizer.
  * **Normalization:** \* Stopword removal (common English words).
      * Case folding (lowercasing).
      * Noise filtering (removing special characters/symbols).
  * **Stemming:** Implements the **Porter Stemmer** algorithm to reduce words to their root forms.

### 🔎 Search & Ranking Logic

  * **Inverted Index:** A high-performance mapping of `Terms -> Document IDs` for rapid lookups.
  * **TF-IDF Weighting:** Calculates Term Frequency and Inverse Document Frequency using `scikit-learn`.
  * **Vector Space Model:** Ranks results based on **Cosine Similarity** between the user query and document vectors.

-----

## 📂 Project Structure

```text
project/
├── scraper.py              # Web crawler (BeautifulSoup4)
├── indexer.py              # Inverted index construction logic
├── searchData.py           # Ranking & retrieval engine
├── text_processing.py      # Shared NLP utility module
├── tfidf_model.py          # TF-IDF vectorization logic
├── web_app.py              # Flask server & API routes
├── data/                   # Generated data files (JSON)
│   ├── scraper_results.json
│   ├── publication_indexed_dictionary.json
│   └── publication_list_stemmed.json
└── templates/              
    └── index.html          # Search engine frontend
```

-----

## 🚀 Getting Started

### 1\. Prerequisites

Ensure you have Python 3.8+ installed. Install the required dependencies:

```bash
pip install flask nltk beautifulsoup4 scikit-learn requests
```

### 2\. Download NLTK Models

The system requires specific language models for tokenization and stemming:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 3\. Execution Pipeline

Run the components in the following order to build the index and launch the app:

```bash
# Step 1: Scrape the data
python scraper.py

# Step 2: Build the index and TF-IDF vectors
python indexer.py

# Step 3: Start the web server
python web_app.py
```

### 4\. Access the UI

Open your browser and navigate to:
`http://127.0.0.1:5000`

-----

## 📊 Example Queries

Try the following terms in the search bar:

  * `machine learning`
  * `python security`
  * `linux internals`
  * `cryptography`

-----

## 🛠️ Tech Stack

  * **Backend:** Python, Flask
  * **NLP:** NLTK (Natural Language Toolkit)
  * **Scraping:** BeautifulSoup4, Requests
  * **ML/Math:** Scikit-learn, NumPy

-----

## 🧪 Limitations & Roadmap

### Current Constraints

  * **Ranking:** Uses basic TF-IDF (lacks BM25 probabilistic ranking).
  * **Scale:** Optimized for small datasets; not suitable for millions of documents.
  * **Querying:** No support for phrase search (e.g., "exact match") or Boolean operators.

### Future Enhancements

  - [ ] Implement **BM25 Ranking** for better relevance.
  - [ ] Add **Query Suggestion** (Autocomplete) functionality.
  - [ ] Support **Positional Indexing** for phrase search.
  - [ ] Integrate **Elasticsearch** for high-scalability production use.
