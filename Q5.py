import requests

url = 'http://mercury.picoctf.net:1270'

params = { 'User-Agent' : 'PicoBrowser', 'Referer':'mercury.picoctf.net:1270 ','Date':'2018'
          ,'DNT':'1','X-Forwarded-For': '92.34.186.83', 'Accept-Language':'sv-SWE'}

r = requests.get(url, headers=params)

print(r.text)