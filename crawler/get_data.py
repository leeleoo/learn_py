# coding utf8
import urllib2
import json


def get_data (url):
	response = urllib2.urlopen(url)
	return json.loads(response.read())['data']['items']
