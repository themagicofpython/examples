import requests
url = 'https://facebook.com'
r = requests.get(url)
for cookie in r.cookies:
	print(cookie.name, cookie.value)
