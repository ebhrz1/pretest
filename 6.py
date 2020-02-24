#!/usr/bin/python3
#10*10 棋盘
import random
def print_map(game_map,steps,player):
	for i in game_map:
		for j in i:
			if j == steps:
				print(j,player,end='')
			else:
				print(j,'*',end='')
			print('\t',end='')
		print()
game_map=[]
for i in range(10):
	tmp=list(range((9-i)*10+1,(10-i)*10+1))
	if i%2 == 0:
		tmp.reverse()
	game_map.append(tmp)
p1=0
p2=0
while True:
	input('player 1 roll,press enter:')
	roll=random.randint(1,6)
	print('player 1 roll',roll)
	p1+=roll
	if p1 >= 100:
		flag=1
		break
	if p1%10 == 5:
		print('move forward 9 steps')
		p1+=9
	elif p1%10 == 0:
		print('oops,back to the start')
		p1=0
	print('now p1 is at',p1)
	print_map(game_map,p1,'p1')

	input('player 2 roll,press enter:')
	roll=random.randint(1,6)
	print('player 2 roll',roll)
	p2+=roll
	if p2 >= 100:
		flag=2
		break
	if p2%10 == 5:
		print('move forward 9 steps')
		p2+=9
	elif p2%10 == 0:
		print('oops,back to the start')
		p2=0
	print('now p2 is at',p2)
	print_map(game_map,p2,'p2')
if flag == 1:
	print('player1 wins')
else:
	print('player2 wins')