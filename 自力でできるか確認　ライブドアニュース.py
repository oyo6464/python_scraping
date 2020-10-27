import requests
from bs4 import BeautifulSoup

"""
自力でもスクレイピングできるか練習 403でてしまった
ライブドアニュース
https://news.livedoor.com/
"""
url = "https://news.livedoor.com/"
a = requests.get(url)
print(a.status_code)
s = BeautifulSoup(a.content,"html.parser")
#print(s)

#midasi = s.find(class_="topicsList")
#print(midasi)


#for taitoru in midasi.find_all("a"):
   # print(taitoru.text)
