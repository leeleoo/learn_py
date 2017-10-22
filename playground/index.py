# -*- coding:utf-8 –*-

index_list = [1,2,3,8,4,5,5,6,7]

index = 0
def change_data():
	global index
	index += 1
	if(len(index_list) - 1 < index):
		print '完毕'
	else:
		print index_list[index]
		change_data()

change_data()