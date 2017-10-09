# coding utf8
import urllib2, cookielib

'6-13,15,20,47,30,38'
url = 'https://www.bevol.cn/product?category=13'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


def get_html(_url = url):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	request = urllib2.Request(_url)

	urllib2.install_opener(opener)

	request.add_header('User-Agent', ua)

	response = urllib2.urlopen(request)

	return response.read()
