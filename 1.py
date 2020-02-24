#!/usr/bin/python3
import datetime
utc=input('input a utc time:')
tz=input('input the time timezone:(support Pacific Mountain Central Eastern China BST)')
utc=datetime.datetime.strptime(utc,'%d/%m/%Y %H:%M')
tzdict={'Pacific':-8,'Mountain':-7,'Central':-6,'Eastern':-5,'China':8,'BST':1}
try:
	target=utc+datetime.timedelta(hours=tzdict[tz])
	print(target.strftime('%d/%m/%Y %H:%M'))
except:
	print('this timezone not defined')