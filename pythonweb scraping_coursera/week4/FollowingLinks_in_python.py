import urllib.request
from bs4 import BeautifulSoup
sample_url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'

for i in range(4):
    
    url=urllib.request.urlopen(sample_url).read()
    soup=BeautifulSoup(url,'html.parser')
    tags=soup.findAll('a')[2]
    sample_url=tags.get('href',None)
print(tags)
print(tags.text)


actual_url='http://py4e-data.dr-chuck.net/known_by_Aleksandra.html'
#actual_url 
for i in range(7):
    
    url=urllib.request.urlopen(actual_url).read()
    soup=BeautifulSoup(url,'html.parser')
    tags=soup.findAll('a')[17]
    actual_url=tags.get('href',None)
print(tags)
print(tags.text)
