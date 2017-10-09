# coding utf8
from open_url import (get_html)
from html_parser import (parse_product_list)
from urls import (get_url)
from get_data import (get_data)
from write_in_csv import write_list


def main():
	product_list = get_data(get_url())
	print product_list[0].keys()
	write_list(product_list)
	#html_doc = get_html(get_url())

	#print parse_product_list(html_doc)


main()