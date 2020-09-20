import requests #Requests がWebサイトからWebページを取得するライブラリ
from bs4 import BeautifulSoup #Beautiful Soup がWebページを解析して情報を抽出するライブラリ

# WebサイトのURLを指定
url = "https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja"

# Requestsを利用してWebページを取得する
r = requests.get(url)

# BeautifulSoupを利用してWebページを解析する
soup = BeautifulSoup(r.text, 'html.parser')

# soup.find_allを利用して、ヘッドラインのタイトルを取得する
elems = soup.find_all("a")
for e in elems:
    print(e.getText())