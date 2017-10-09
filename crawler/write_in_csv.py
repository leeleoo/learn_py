# -*- coding:utf-8 –*-
import unicodecsv


def write_list(value):
	with open("./data/product_list.csv", "a+") as csvfile:
		fieldnames = value[0].keys()
		writer = unicodecsv.DictWriter(csvfile,fieldnames=fieldnames)
		#writer.writeheader()
		writer.writerows(value)
