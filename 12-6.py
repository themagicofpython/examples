import requests
url = 'https://httpbin.org/cookies'
cookies = dict(cookie_test = 'successful')
r = requests.get(url, cookies=cookies)
print(r.text)
