# file = open("D:/IR/Term-Document_Matrix/index.txt", 'r')

# my_dict = {} # tạo dictionary rỗng

# for line in file:
#     columns = line.strip().split() # tách dòng thành các cột
#     key = columns[0] # cột đầu tiên làm key
#     values = columns[2:] # các cột còn lại làm value
#     my_dict[key] = values # thêm key và value vào dictionary
# file.close() # đóng file

# def search(a, my_dict):
#     return(my_dict[a])

# def Intersection(a,b, my_dict):
#     word2 = my_dict[a]
#     word1 = my_dict[b]
#     ans = []
#     i = j = 0

#     while i < len(word1) and j < len(word2):
#         if word1[i] < word2[j]:
#             i += 1
#         elif word1[i] > word2[j]:
#             j += 1
#         else:
#             ans.append(word1[i])
#             i += 1
#             j += 1
#     return ans

# def Union(a, b, my_dict):
#     word1 = my_dict[a]
#     word2 = my_dict[b]
#     ans = []
#     i = j = 0

#     while i < len(word1) and j < len(word2):
#         if word1[i] < word2[j]:
#             ans.append(word1[i])
#             i += 1
#         elif word1[i] > word2[j]:
#             ans.append(word2[j])
#             j += 1
#         else:
#             ans.append(word1[i])
#             i += 1
#             j += 1

#     while i < len(word1):
#         ans.append(word1[i])
#         i += 1

#     while j < len(word2):
#         ans.append(word2[j])
#         j += 1

#     return ans

# def tru(a,b,my_dict):
#     word2 = ['d1', 'd2', 'd4']
#     word1 = ['d0', 'd1', 'd2']
#     ans = []
#     i = j = 0

#     while i < len(word1) and j < len(word2):
#         if word1[i] < word2[j]:
#             ans.append(word1[i])
#             i += 1
#         elif word1[i] > word2[j]:
#             j += 1
#         else:
#             i += 1
#             j += 1

#     while i < len(word1):
#         ans.append(word1[i])
#         i += 1
#     return ans

# def orNot(a,b,my_dict):
#     ans = []

#     for key, value in my_dict.items():
#         if key != a and key != b:
#             ans.extend(my_dict[key])

#     result = list(set(ans) - set(my_dict[b]))
#     result.extend(my_dict[a])

#     return (list(set(result)))  

# def ornot(a,b,my_dict):
#     # word1 = ['d1', 'd4', 'd8', 'd10']
#     # word2 = ['d1', 'd4', 'd7']
#     # dog = ['d1', 'd7', 'd11', 'd13']
#     # cat = ['d2', 'd4', 'd7']
#     # word1 = my_dict[a]
#     # word2 = my_dict[b]
#     my_dict = {
#         'word1': ['d1', 'd4', 'd8', 'd10'],
#         'word2': ['d1', 'd4', 'd7'],
#         'dog': ['d1', 'd7', 'd11', 'd13'],
#         'cat': ['d2', 'd4', 'd7']
#     }
#     ans = []
#     for key, value in my_dict.items():
#         if key != a and key != b:
#             ans.extend(my_dict[key])

#     result = list(set(ans) - set(my_dict['word2']))
#     result.extend(my_dict['word1'])

#     print(list(set(result)))


# # print(search("a", my_dict))
# # print(Intersection("trade", "said", my_dict))
# # print(Union("product", "mln", my_dict))
# print(orNot("said", "trade",my_dict))
# print(type(my_dict['a']))

# =====================================================
# from bs4 import BeautifulSoup
# import requests
# import trafilatura
# import json

# url = 'https://baomoi.com/cntt-vien-thong.epi'
# response = requests.get(url)
# html_content = response.text

# soup = BeautifulSoup(html_content, "html.parser")

# articles = []

# for link in soup.find_all('a', href=True):
#     href = link['href']
#     absolute_url = href if href.startswith(('http://', 'https://')) else f"{url}/{href}"
#     try:
#         # response = requests.get(absolute_url)
#         # content = trafilatura.extract(response.text)

#         response = requests.get(absolute_url)
#         html = response.text
#         content = trafilatura.extract(html)

#         articles.append({
#             "url": absolute_url,
#             "content": content,
#             "date": ""  # cần cung cấp thêm thông tin ngày tháng của bài viết
#         })
#     except:
#         print(f"Failed to crawl: {absolute_url}")

# with open("chus.json", "w", encoding="utf-8") as f:
#     json.dump(articles, f, ensure_ascii=False, indent=4)
# =====================================================

import trafilatura
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Lấy HTML từ một trang web bất kỳ
url = "https://baomoi.com/bao-mat/t/16541557.epi"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
# print(soup)

links = set()
for link in soup.find_all('a'):
    href = link.get('href')
    # links.add(href)
    if href and (href.startswith('http') or href.startswith('https')):
        absolute_url = href
    else:
        absolute_url = urljoin(url, href)
    links.add(absolute_url)
    # print(href)

for i in links:
    print(i)


# Sử dụng trafilatura để trích xuất nội dung từ HTML
# extracted_content = trafilatura.extract(html)

# print(extracted_content)



