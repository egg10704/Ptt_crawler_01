Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/joke/index.html"
for i in range(3): #往上爬3頁
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.title a") #標題
u = soup.select("div.btn-group.btn-group-paging a") #a標籤
print ("本頁的URL為"+url)
url = "https://www.ptt.cc"+ u[1]["href"] #上一頁的網址

for s in sel: #印出網址跟標題
print(s["href"],s.text)