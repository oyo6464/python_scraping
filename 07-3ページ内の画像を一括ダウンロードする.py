import requests
from bs4 import BeautifulSoup
import time
from  pathlib import Path
import urllib
#pathlib　のPathでフォルダを作る
#urllib　で絶対パスを作る

#webページの取得 bsで解析  
url = "https://www.ymori.com/books/python2nen/test2.html"
a = requests.get(url)
s = BeautifulSoup(a.content,"html.parser")

#保存用フォルダ
out_folder  = Path("07-3ダウンロードフォルダ")
out_folder.mkdir(exist_ok = True)



#print(s) 確認用
#img タグを回して　srcタグでurlを取得する(相対パスも混在)
#print(s.find_all("img")) #確認用

for i in s.find_all("img"):
    src_tagdayo = i.get("src")
    #print(src_tagdayo)

   #絶対URLを作る  
    #リクエストのゲットモジュールで　画像取得
    img_url = urllib.parse.urljoin(url,src_tagdayo)
    gazou = requests.get(img_url)

    #保存用フォルダ
    #変数 = 保存用フォルダ.joinpath(ファイルネーム) で住所つくる
    #この住所はwith openで使う
    filename = img_url.split("/")[-1] #filename=sample1.png等
    out_pathdayo = out_folder.joinpath(filename)#07-3ダウンロードフォルダ\sample1.png とか
    #print(out_pathdayo) #確認用
"""
    #画像書き込み
    with open(out_pathdayo,"wb") as f:
        f.write(gazou.content)
    time.sleep(1)
"""
