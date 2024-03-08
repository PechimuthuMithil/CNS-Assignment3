import requests

url = 'http://mercury.picoctf.net:1270'

params = { 'User-Agent' : 'PicoBrowser', 'Referer':'mercury.picoctf.net:1270 ','Date':'Tue, 15 Nov 2018 08:12:31 GMT'
          ,'DNT':'1','X-Forwarded-For': '31.3.152.55', 'Accept-Language':'sv'}

r = requests.get(url, headers=params)

print(r.text)