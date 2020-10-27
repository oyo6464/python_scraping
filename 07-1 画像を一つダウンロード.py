import requests
from pathlib import Path 


#保存用ファイル作成
of = Path("07画像ダウンロード")
of.mkdir(exist_ok=True) #ダウンロードファイルを作る


image_url = "https://www.ymori.com/books/python2nen/sample1.png"
a = requests.get(image_url)

#確認用
#filename0 = image_url.split("/")
#print(filename0)

filename = image_url.split("/")[-1]
#print(filename)

#フォルダ名を連結
op = of.joinpath(filename) #opは..画像ダウンロード/sample1.png みたいになってるはず
#print(op)

#mkdirで作った画像ダウンロードフォルダにsample1.pngを書き込む
#opが保存するファイルの住所みたいなもの
with open(op,"wb") as f:
    f.write(a.content)
