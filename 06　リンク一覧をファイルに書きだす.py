import requests
from bs4 import BeautifulSoup
import urllib

"""https://www.ymori.com/books/python2nen/test2.html"""

url = "https://www.ymori.com/books/python2nen/test2.html"
a = requests.get(url)
b = BeautifulSoup(a.content,"html.parser")
#確認用
#print(b)


filename = "06リンクテキスト.txt"
with open(filename,"w") as f:
    
    for i in b.find_all("a"):
        print(i.text)
        #print(i) #確認用
        x = i.get("href")
        #print(x) #確認用　これやと相対URLと絶対URLが入り混じってるかも
        #相対URがあるかもしれんから絶対URLを取得する
        link_x = urllib.parse.urljoin(url,x)
        print(link_x)

        f.write(i.text+"\n")
        f.write(link_x+"\n")
        f.write("\n")
    f.write("このテキストは06 リンク一覧をファイルに書き出す.pyからの自動生成")
