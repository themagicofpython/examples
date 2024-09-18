import requests
headers = {'user-agent': 'python scraper 0.1'}
data = {'key':'value'}
r = requests.post('http://httpbin.org/post', headers = headers, data = data)
