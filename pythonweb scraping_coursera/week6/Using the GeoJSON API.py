import urllib.request
import json
api_key=False
if api_key is False:
    api_key=42
    ser='http://py4e-data.dr-chuck.net/json?'
while True:
    loc=input("enter location")
    p={}
    p['address']=loc
    if api_key is not False:
        p['key']=api_key
    url=ser+urllib.parse.urlencode(p)
    print(url)
    #print("Retrving url")
    url_open=urllib.request.urlopen(url)
    data=url_open.read().decode()
    #print(len(data))
    js=json.loads(data)
    #print(js)
    print(js['results'][0]['place_id'])
