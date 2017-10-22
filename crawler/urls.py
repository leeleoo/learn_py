# coding utf8
from furl import furl

base_url = 'https://api.bevol.cn/search/goods/index3?p=0&keywords=&category=11&state=1'

category_index_list = [30,38]

def get_url(index,p):

	global base_url

	f = furl(base_url)

	f.args['p'] = p

	f.args['category'] = category_index_list[index]

	base_url = f.url

	print 'current',base_url

	return base_url
