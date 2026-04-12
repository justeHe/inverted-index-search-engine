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

    # ⭐ 更通用写法（避免 class 变化导致崩）
    books = soup.select("article, div.view-content div")

    for item in books:
        try:
            a_tag = item.find("a")
            if not a_tag or not a_tag.text.strip():
                continue

            name = a_tag.text.strip()
            link = a_tag.get("href", "")

            # 处理相对路径
            if link.startswith("/"):
                link = "https://nostarch.com" + link

            # 作者（可能不存在）
            author_tag = item.find(string=lambda x: x and "by" in x.lower())
            author = author_tag.strip() if author_tag else "Unknown"

            data = {
                "link": link,
                "name": name,
                "author": author
            }

            book_data.append(data)

        except Exception:
            continue

    # 去重（防止抓重复）
    unique_data = {item['name']: item for item in book_data}.values()

    with open('scraper_results.json', 'w', encoding='utf-8') as f:
        json.dump(list(unique_data), f, ensure_ascii=False, indent=2)

    print(f"✅ Crawled {len(unique_data)} books")

if __name__ == "__main__":
    startScraper()