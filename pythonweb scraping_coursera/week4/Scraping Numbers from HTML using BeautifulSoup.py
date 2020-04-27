import urllib.request
from bs4 import BeautifulSoup
url=input("Enter url")
url_open=urllib.request.urlopen(url).read()
soup=BeautifulSoup(url_open,'html.parser')
tags=soup('span')
s=0
for i in tags:
    s+=int(i.text)
print(s)
