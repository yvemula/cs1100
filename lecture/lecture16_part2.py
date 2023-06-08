# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:17:04 2022

@author: Yathin Vemula
"""

i=input('Enter the name of the IMDB file ==> ')
i=i.strip()
print(i)
d=dict()
f=open(i,encoding='ISO-8859-1')
for x in f:
    w=x.strip().split('|')
    n=w[0].strip()
    if n in d:
        d[n]+=1
    elif n not in d:
        d[n]=1
n=sorted(d)
lim = min(100,len(n))
for j in range(lim):
    na = n[j]
t=list(d.values())
num = sorted(t)[len(t)-1]
for g in range(len(t)):
    if(t[g]==num):
        break
key = list(d.keys())
pos = key[g]
c=0
for v in t:
    if v==1:
        c+=1
print('{} appears most often: {} times'.format(pos,num))
print('{} people appear once'.format(c))