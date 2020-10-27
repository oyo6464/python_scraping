import requests
from bs4 import BeautifulSoup
import urllib

"""https://www.ymori.com/books/python2nen/test2.html
"""

url = "https://www.ymori.com/books/python2nen/test2.html"
a = requests.get(url)
s = BeautifulSoup(a.content,"html.parser")
#print(s)

for i in s.find_all("img"):
    src = i.get("src")
    #print(src)

    zettaiurl = urllib.parse.urljoin(url,src)
    #print(zettaiurl) #画像urlの完成
    gazou = zettaiurl.split("/")[-1]
    print(gazou,">>",zettaiurl)
