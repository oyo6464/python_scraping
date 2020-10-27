import requests
from bs4 import BeautifulSoup 
"""
今回はヤフーのITニュースのurlを使ってスクレイピングする
https://news.yahoo.co.jp/categories/it
"""

#まずは取得
url = "https://news.yahoo.co.jp/categories/it"
a = requests.get(url)

#bsで解析する
s = BeautifulSoup(a.content,"html.parser")
#トピックスとの所までをとってくる
taitorutati = s.find(class_="topicsList_main")

#この中のaタグ確認用
#print(taitorutati.find_all("a"))

#ここからaタグのテキストだけとってくる 
for taitoru in taitorutati.find_all("a"):
    print(taitoru.text)
