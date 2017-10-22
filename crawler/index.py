# -*- coding:utf-8 –*-
from open_url import (get_html)
from html_parser import (parse_product_list)
from urls import (get_url,category_index_list)
from get_data import (get_data)
from write_in_csv import write_list
import time
from db import get_db_connection, insert

url_index = 0
p = 250


def init ():
	global url_index,p
	p += 1
	product_list = get_data(get_url(url_index,p))
	if len(product_list) > 0:
		insert(conn = conn, data = product_list)
		time.sleep(1)
		init()
	else:
		url_index += 1
		p = 0
		if(len(category_index_list) -1 < url_index):
			conn.close()
		else:
			init()

conn = get_db_connection()
init()
