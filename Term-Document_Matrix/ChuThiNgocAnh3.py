from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import trafilatura
import json
from datetime import datetime

# Lấy nội dung html
url = 'https://baomoi.com/van-hoa.epi'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# Tìm thẻ a trong html
links = set()
for link in soup.find_all('a'):
    href = link.get('href')
    if href.startswith('http') or href.startswith('https'):  
        urls = href
    else:
        urls = urljoin(url, href)
    links.add(urls)

# Lấy nội dung chính của các bài viết từ URL bằng trafilatura
news = []
date = str(datetime.now())

for link in links:
        response = requests.get(link)
        content = trafilatura.extract(response.text)

        news.append({
            "url": link,
            "content": content,
            "date": date
        })

# Viết ra file json
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=4)
    