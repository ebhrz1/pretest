#!/usr/bin/python3
phone_dict={
	'Apple':{'iphone 11 pro':1200,'iphone XS':800,'iphone 11':700,'iphone XR':600,'iphone X':600},
	'Huawei':{'mate 30 pro':900,'mate 30':800,'p30 pro':700,'p30':600},
	'Samsung':{'S13':900,'S12':800,'S11':700}
}
def find_phone(brand,money):
	if brand in phone_dict:
		for name,price in phone_dict[brand].items():
			if price > money:
				continue
			else:
				print('you can choose',name,'and you will remain',money-price)
				break
	else:
		print('no such brand in database')
brand=input('input a brand:')
money=int(input('input your maximum price:'))
find_phone(brand,money)