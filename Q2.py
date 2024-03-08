import requests

def get_flag(lis):
    for i in range(len(lis)):
        if (lis[i] == 'flag:'):
            return lis[i+1]
        
url1 = 'http://jupiter.challenges.picoctf.org:44924/'
url2 = 'http://jupiter.challenges.picoctf.org:44924/mycss.css'
url3 = 'http://jupiter.challenges.picoctf.org:44924/myjs.js'

a = requests.get(url1).text.split()
b = requests.get(url2).text.split()
c = requests.get(url3).text.split()

print("Flag = ",get_flag(a)+get_flag(b)+get_flag(c))