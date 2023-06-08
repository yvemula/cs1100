# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:01:53 2022

@author: Yathin Vemula
"""
for i in range(9):
	print(i, end=' ')
for i in range(9):
	for j in range(9):
		if (j+1)%3==0:
			print(str(i)+','+str(j), end='  ')
		else:
			print(str(i)+','+str(j), end=' ')
	if (i+1)%3==0:
		print("\n")
	else:
		print()
for i in range(9):
	if i == 2:
		for j in range(9):
			print(str(i)+','+str(j), end=' ')
for i in range(9):
	for j in range(9):
		if j == 5:
			print(str(i)+','+str(j), end=' ')
for i in range(9):
	if i <= 2:
		for j in range(9):
			if j <= 2:
				print(str(i)+','+str(j), end=' ')
		print()