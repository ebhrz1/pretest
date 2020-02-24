#!/usr/bin/python3
import datetime
date=input('input a date:')
birth=input('input a birth:')
date=datetime.datetime.strptime(date,'%d/%m/%Y')
birth=datetime.datetime.strptime(birth,'%d/%m/%Y')
i=0
while date > birth:
	date=date.replace(year=date.year-1)
	i+=1
print(i-1,'years old')
#如果直接用相差天数除以365会在极端情况下造成闰年时间差，导致岁数有问题，所以循环之后用自带的比较方啊比较