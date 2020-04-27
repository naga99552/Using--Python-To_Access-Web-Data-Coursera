import urllib.request
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET

#find sample data sum
sample_data='http://py4e-data.dr-chuck.net/comments_42.xml'
def sample_sum():
    count_sample_sum=0
    url=urllib.request.urlopen(sample_data)
    data=url.read()
    #print(data)
    tree=ET.fromstring(data)
    path=tree.findall('comments/comment')
    #print(tree)
    for i in path:
        count_sample_sum+=int(i.find('count').text)
    print(count_sample_sum)
sample_sum()


#find actual data sum
actual_data='http://py4e-data.dr-chuck.net/comments_169943.xml'
def actual_sum():
    count_actual_sum=0
    url=urllib.request.urlopen(actual_data)
    data=url.read()
    #print(data)
    tree=ET.fromstring(data)
    path=tree.findall('comments/comment')
    #print(tree)
    for i in path:
        count_actual_sum+=int(i.find('count').text)
    print(count_actual_sum)
actual_sum()
