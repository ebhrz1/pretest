#!/usr/bin/python3
import time
animal_dict=['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Goat']
date=input('input a date of birth:')
date=time.strptime(date,'%d/%m/%Y')
print(animal_dict[date.tm_year%12])
