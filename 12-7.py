import requests
url = 'https://facebook.com'
r = requests.get(url)
jar = requests.cookies.RequestsCookieJar()
for cookie in r.cookies:
	jar.set(cookie.name, cookie.value, domain = cookie.domain, path = cookie.path)
r = requests.get(url, cookies=jar)
print(r.text)
