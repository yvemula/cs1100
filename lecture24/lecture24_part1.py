# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:22:03 2022

@author: Yathin Vemula
"""
def absolute(n):
    return abs(n)
values = [-12,0,15,-16,-17.3,8,4,-5]
new_values = list(map(absolute,values))
print(new_values)