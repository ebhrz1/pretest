#!/usr/bin/python3
even_list=[]
try:
	while True:
		tmp = input('please input a integer or ctrl-c to stop:')
		if int(tmp) % 2 == 0:#even
			even_list.append(int(tmp))
			print('the list now has',even_list)
		else:
			print('ignore')
except:
	print('stop')
print('the sum is',sum(even_list))