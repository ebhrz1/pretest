#!/usr/bin/python3
import random
question=[0 for i in range(14)]
for i in range(10):#each of 10 studentts
	num=random.randint(1,14)
	ques=[i for i in range(14)]
	random.shuffle(ques)#通过shuffle方式来随机所有题目，之后只需pop就可以随机得到题目，避免random出来的数字重复
	for j in range(num):
		question[ques.pop()]+=1
for i in range(len(question)):
	print('question',i+1,'answered',question[i],'times')