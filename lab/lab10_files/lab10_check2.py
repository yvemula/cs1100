# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:11:14 2022

@author: Yathin Vemula
"""
def closest2(list):
    '''
       addone(x) returns 1 more than
       the value x passed in.

       >>> closest2([15.1,-12.1,5.4,11.8,17.4,4.3,6.9])
       (5.4, 4.3)
       '''
    difference = 10**10
    (x,y)=(0,0)
    i = 0
    list1 = list[0:]
    list1.sort()
    while (i + 1) < (len(list1) - 1):
        diff = abs(list1[i] - list1[i + 1])
        if diff < difference:
            difference = diff
            (x,y) = (list1[i], list1[i+1])
        i += 1
    return (y,x)

if __name__ == "__main__":
    
    L1=[15.1,-12.1,5.4,11.8,17.4,4.3,6.9]
    (x,y)=closest2(L1)
    print(y,x)