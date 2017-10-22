# -*- coding:utf-8 –*-
import unicodecsv


def write_list (value):
	with open("./data/product_list.csv", "a+") as csvfile:
		writer = unicodecsv.DictWriter(csvfile)
		writer.writerows(value)
