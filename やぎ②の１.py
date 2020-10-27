import requests
"""
https://www.ymori.com/books/python2nen/test1.html
requestsでhtmlを取得し、テキストファイルとして書きだす練習

"""


url = "https://www.ymori.com/books/python2nen/test1.html"
a = requests.get(url) #サイトページ取得
a.encoding = a.apparent_encoding#エンコをとってきた文字コードと同じの指定
print(a.text)#.textを付けると文字でだせる

#補足
#print(a.url)#url出せる
#print(a.content)#バイナリ出る
#print(a.apparent_encoding)#文字コードでる
#print(a.status_code) #httpステータスコード 200はOK 404はnot found
#print(a.headers)#レスポンスヘッダー 

#ファイルがない時に実行すると、このpyファイルが存在するディレクトリにdownload.text　ファイルができる
filename = "download.text"
with open(filename,"w") as f:
    f.write(a.text)
    f.write("このテキストファイルはやぎ②の１から自動で書き込んでいる")
