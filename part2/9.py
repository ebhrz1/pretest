def shape_data(shape,*args):
	if shape == 'circle':
		print('area:',3.142*args[0]*args[0])
		print('circumference:',2*3.142*args[0])
	elif shape == 'rectangle':
		print('area:',args[0]*args[1])
		print('circumference:',2*(args[0]+args[1]))
	else:
		print('unknown shape')
shape_data('circle',15)
shape_data('rectangle',10,5)