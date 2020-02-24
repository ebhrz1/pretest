#!/usr/bin/python3
str1=input('please input string 1:')
str2=input('please input string 2:')
i=1
min_len=min(len(str1),len(str2))
while i < min_len:
	'''
	使用异或交换
	str1=str1[:i] + chr(ord(str1[i]) ^ ord(str2[i])) +str1[i+1:]
	str2=str2[:i] + chr(ord(str1[i]) ^ ord(str2[i])) +str2[i+1:]
	str1=str1[:i] + chr(ord(str1[i]) ^ ord(str2[i])) +str1[i+1:]
	'''
	tmp1=str1[i]
	tmp2=str2[i]
	str1=str1[:i] + tmp2 +str1[i+1:]
	str2=str2[:i] + tmp1 +str2[i+1:]
	i+=2
print(str1[:min_len])
print(str2[:min_len])