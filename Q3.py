import requests

url = 'https://jupiter.challenges.picoctf.org/problem/29835/'
r = requests.get(url)

print(r.text)