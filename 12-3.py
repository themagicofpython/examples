import requests

def download_page(url):
	r = requests.get(url)
	return r.text

API_key = 'XXXXXXXXXXXXXXXXXXXXX'
f = open('weather.json','w')
answer = download_page('http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID='+API_key)
f.write(answer)
f.close() 
