# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:03:31 2022

@author: Yathin Vemula
"""

l1=[15.1,-12.1,5.4,11.8,17.4,4.3,6.9]
def closest1(L1):
 '''
    addone(x) returns 1 more than
    the value x passed in.

    >>> closest1([15.1,-12.1,5.4,11.8,17.4,4.3,6.9])
    (5.4, 4.3)
    '''
 closest = (None, None)
 for i in range(len(L1)):
     for j in range(len(L1)):
         if i != j and L1[i] <= L1[j] and (closest[0] is None or L1[j] - L1[i] <closest[1] - closest[0]):
             closest = (L1[i], L1[j])
 return closest[1],closest[0]    

(x,y) = closest1(l1)
print(y,x)