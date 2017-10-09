# -- coding utf8 --
from bs4 import BeautifulSoup


def parse_product_list(html_doc):
	print(html_doc)
	soup = BeautifulSoup(html_doc, 'html.parser',from_encoding = 'utf8')
	page_content = soup.find(class_="page-content")
	print 'contents',page_content.contents
	for child in page_content.children:
		print (child)

	return page_content

