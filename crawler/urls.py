# coding utf8
from furl import furl

base_url = 'https://api.bevol.cn/search/goods/index3?p=1&keywords=&category=7&state=1'


def get_url(url = base_url):

	f = furl(url)

	old_p = int(f.args['p'])

	new_p = old_p + 1

	f.args['p'] = new_p

	base_url = f.url

	return base_url
