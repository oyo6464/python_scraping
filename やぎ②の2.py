import requests
from bs4 import BeautifulSoup
"""
https://www.ymori.com/books/python2nen/test1.html
https://www.ymori.com/books/python2nen/test2.html
BeautifulSoupの使い方、find やfind_allの使い方を練習
52,53行目辺りでid指定してるけど、b.find(class_="") とするとclassも切り出せる
"""



url = "https://www.ymori.com/books/python2nen/test1.html"
x = requests.get(url)

#aにhtmlを解析したやつを代入（取ってきたurl,htmlを解析する(解析するもの=parser)）
a = BeautifulSoup(x.content,"html.parser")

#解析済みのhtmlが出力される（全部）
#print(a)

#解析済み.find(指定したいタグ)で絞れる
#print(a.find("title"))
#print(a.find("h2"))
#print(a.find("li"))

#タグの中の文字だけほしい時 textをつける
#print(a.find("title").text)
#print(a.find("head"))
#print(a.find("body").text)






url2 = "https://www.ymori.com/books/python2nen/test2.html"
y = requests.get(url2)
b = BeautifulSoup(y.content,"html.parser")
#ここまで上と同じ
#print(b)

#find だとそのタグのひとつめのみ
#print(b.find("li"))

#find_all　を使うとそのタグすべてをリストに格納してくれる
#print(b.find_all("li"))

#リストだからfor　使ったほうがみやすい textつけてタグも外す
"""
for li_tag in b.find_all("li"):
    print(li_tag.text)
"""
#上のままだと1章と2章のliタグがでるので絞り込む まずは2章全部出してみる
#print(b.find_all(id="chap2"))
#print(b.find(id="chap2")) #この２つ　どう違うかというと、リストに入ってるか入ってないか

#その前に2章を変数にいれる その後forで繰り返す シーケンスとして使えるのはfind_allでリストにしたほう

z = b.find(id="chap2") #←ここではfind_allしない　まだリストにしない
for li_tag in z.find_all("li"):
    print(li_tag.text)

