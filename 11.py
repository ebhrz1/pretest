#!/usr/bin/python3
import random
cards=[]
#加入所有牌
for i in range(1,11):
	for j in range(4):
		cards.append(str(i))
for j in range(4):
	cards.append('J')
for j in range(4):
	cards.append('Q')
for j in range(4):
	cards.append('K')
cards.append('Joker')
cards.append('Joker')
#洗牌
random.shuffle(cards)
#发牌 一人一半
p1=cards[:27]
p2=cards[27:]
for i in range(27):
	print('player 1 plays',p1[i])
	print('player 2 plays',p2[i])
	if p1[i] == p2[i]:
		print('snap!')
		break
	else:
		print('next round')
print('game end')