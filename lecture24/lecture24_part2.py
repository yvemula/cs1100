# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:27:47 2022

@author: Yathin Vemula
"""

points = [ (4,2), (1,-3), (-4, -6), (6,9), (3,8), (-5,2), (6,2) ]
def fun(i):
    if(i[0]>0 and i[1]>0):
        return True;
    else:
        return False;
            
points=filter(fun,points);
print(min(points)[0]);

 