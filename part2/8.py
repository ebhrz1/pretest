#!/usr/bin/python3
filter_words = ['the','of','and','a','to', 'in', 'is', 'you', 'that', 'it', 'he', 'was','for','on','are','as','with','his','they','I']
filter_dict={}
for i in filter_words:
	filter_dict[i]=0
string=input('input a text,use blank before and after punctuation:\n')
str_list=string.split(sep=' ')
del_list=[]
for i in range(len(str_list)):
	if str_list[i] in filter_words:
		filter_dict[str_list[i]]+=1
		del_list.append(i)
for i in range(len(str_list)):
	if i not in del_list:
		print(str_list[i],end=" ")
print()
for key , val in filter_dict.items():
	print(key,':',val)