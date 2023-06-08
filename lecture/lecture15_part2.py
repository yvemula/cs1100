# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:24:23 2022

@author: Yathin Vemula
"""

file = input("Data file name: ").strip()
print(file)

prefix = input("Prefix: ").strip()
print(prefix)
names = set()
count = 0
for line in open(file,encoding = "ISO-8859-1"):
     words = line.strip().split('|')
     fullName = words[0].strip().split(',')
     lastName = fullName[0]
     if not lastName in names:
         names.add(lastName)
         
for x in names:
    if x.startswith(prefix) ==  True:
        count+=1
print(len(names),'last names')
print(count,'start with', prefix)
     

