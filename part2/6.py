#!/usr/bin/python3
import random
def roll():
	a=random.randint(1,6)
	b=random.randint(1,6)
	return a,b,a+b
money=1000
debt=int(input('please bet:'))
if debt > money:
	print("you don't have enough money,auto reset it to the rest of your money")
	debt = money
a,b,num=roll()
print('you roll',a,b,'total:',num)
if num in [7,11]:
	print('you win')
	money+=debt
elif num in [2,3,12]:
	print('you lose')
	money-=debt
else:
	print('tie,game continues')
	while money > 0:
		debt = int(input('please bet:'))
		if debt > money:
			print("you don't have enough money,auto reset it to the rest of your money")
			debt = money
		a,b,tmp=roll()
		print('you roll',a,b,'total',tmp)
		if tmp == 7:
			print('you lose')
			money-=debt
		elif tmp == num:
			print('you win')
			money+=debt
		else:
			print('tie,game continues')
		num=tmp
	print('game over')
