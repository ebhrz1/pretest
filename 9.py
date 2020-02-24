#!/usr/bin/python3
modules={
	'python':{'code':1,'title':'python','teacher':{'Bob':4,'Alice':3}},
	'web':{'code':2,'title':'web','teacher':{'Bob':5,'Alice':2,'Kite':3}},
	'manage':{'code':3,'title':'manage','teacher':{'Kite':7,'Dick':2}},
	'marketing':{'code':4,'title':'marketing','teacher':{'Dick':2,'Alice':3,'Kite':3}}
}
teachers={
	'Alice':{'ID':1,'pay':5},
	'Bob':{'ID':2,'pay':6},
	'Dick':{'ID':3,'pay':4.5},
	'Kite':{'ID':4,'pay':5.5}
}
for teacher_name , teacher_detail in teachers.items():
	total=0
	for module_name , module_detail in modules.items():
		if teacher_name in  module_detail['teacher']:
			total+=teacher_detail['pay']*module_detail['teacher'][teacher_name]
	print(teacher_name,'total',total)