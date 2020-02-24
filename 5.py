#!/usr/bin/python3
forname=input('forname:')
surname=input('surname:')
age=input('age:')
ms=input('marital status:')
gender=input('gender')
gd={'male':1,'female':0}#gender dict
md={'married':1,'single':0}#marry dict
if gd[gender]:
	if age <= 18:
		print('Dear Master',forname,surname)
	else:
		print('Dear MR',forname,surname)
else:
	#Ms Miss Mrs
	if md[ms]:
		print('Dear Mrs',forname,surname)
	else:
		if age <= 18:
			print('Dear Miss',forname,surname)
		else:
			print('Dear Ms',forname,surname)
#瞎写的 就是个决策树if-else