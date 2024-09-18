from lxml import etree
import sys
import json
import requests

def download_page(url):
	r = requests.get(url)
	return r.text
	
def get_articles(context, articles):
	article_dict = {}
	for action, elem in context:
		if not elem.text:
			text = "None"
		else:
			text = elem.text
		article_dict[elem.tag] = text
		if elem.tag == "entry":
			articles.append(article_dict)
			article_dict = {}

def filter_article(article, text):
	if text.encode('utf8').find(article["title"].encode('utf8'))>-1:
		return True
	return False

def download_city(city_str, city_lat, city_lon):
	articles = []
	json_string = download_page('https://en.wikipedia.org/w/api.php?action=query&gslimit=500&format=json&list=geosearch&gsradius=10000&gscoord='+city_lat+'%7C'+city_lon)
	page = download_page('http://en.wikipedia.org/wiki/'+city_str.replace(' ','_'))
	parsed_json = json.loads(json_string)
	for article in parsed_json['query']['geosearch']:
		if filter_article(article, page):
			articles.append(article)
	return articles

if __name__ == "__main__":
	if len(sys.argv)>3:
		city_str=sys.argv[1]
		city_lat, city_lon=sys.argv[2],sys.argv[3]
	else:
		city_str = "Berlin"
		city_lat = '52.52437'
		city_lon = '13.41053'
	articles = download_city(city_str,city_lat,city_lon)
	for article in articles:
		print(article['title'])
