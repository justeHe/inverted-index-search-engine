import json
import requests
from bs4 import BeautifulSoup

URL = "https://nostarch.com/catalog/programming"

def startScraper():
    book_data = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(URL, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("Request failed:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.node-product")

    for item in books:
        try:
            a_tag = item.select_one("h2 a")
            if not a_tag:
                continue

            name = a_tag.text.strip()
            link = a_tag.get("href", "")
            if link.startswith("/"):
                link = "https://nostarch.com" + link

            author_tag = item.select_one(".field-name-field-author .field-item")
            author = author_tag.text.strip() if author_tag else "Unknown"

            summary_tag = item.select_one(".field-name-body .field-item p")
            summary = summary_tag.text.strip() if summary_tag else ""
            
            date_tag = item.select_one(".field-name-field-released .field-item")
            date = date_tag.text.strip() if date_tag else ""

            data = {
                "name": name,
                "link": link,
                "author": author,
                "summary": summary,
                "date": date
            }

            book_data.append(data)

        except Exception as e:
            print("Parse error:", e)
            continue

    unique_data = {item['name']: item for item in book_data}.values()

    with open('scraper_results.json', 'w', encoding='utf-8') as f:
        json.dump(list(unique_data), f, ensure_ascii=False, indent=2)

    print(f"Crawled {len(unique_data)} books")


if __name__ == "__main__":
    startScraper()