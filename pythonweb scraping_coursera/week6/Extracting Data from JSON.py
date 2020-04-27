import json
import urllib.request
def sample_data():
    sample_url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.json')
    data=sample_url.read()
    js=json.loads(data)
    s=0
    for i in js['comments']:
        s+=i['count']
    print(s)
sample_data()



def actual_data():
    actual_url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_169944.json')
    data=actual_url.read()
    js=json.loads(data)
    s=0
    for i in js['comments']:
        s+=i['count']
    print(s)
actual_data()
