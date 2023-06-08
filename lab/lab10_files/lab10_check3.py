# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:14:12 2022

@author: Yathin Vemula
"""
import random
import time
def closest1(list):
 j = 0
 difference = 10**10
 (x,y) = (0,0)
 for item in list:
     i = 0
     for thing in list:
         if i != j:
             diff = abs(item - thing)
             if diff < difference:
                 difference = diff
                 (x,y) = (item,thing)
 
         i += 1
         j += 1
 return (x,y)
 
def closest2(list):
 difference = 10**10
 (x,y) = (0,0)
 i = 0
 list1 = list[0:]
 list1.sort()
 while (i + 1) < (len(list1) - 1):
     diff = abs(list1[i] - list1[i + 1])
     if diff < difference:
         difference = diff
         (x,y) = (list1[i], list1[i+1])
     i += 1
 return (x,y)
 
 
def rand_list(leng):
 list1 = []
 for i in range(leng):
     list1.append(random.uniform(0, 1000))
 return list1
def run_and_time(name1, name2, sort_fcn, sort_fcn2, v):
 print ("Testing " + name1)
 t0 = time.time()
 print (sort_fcn(v))
 t1 = time.time()
 print ("Time: %.4f seconds" %(t1-t0))
 print ("")
 print ("Testing " + name2)
 t0 = time.time()
 print (sort_fcn2(v))
 t1 = time.time()
 print ("Time: %.4f seconds" %(t1-t0))
 
L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
(x,y) = closest1(L1)
print (x, y)
(x,y) = closest2(L1)
print (x, y)
x = rand_list(10000)
run_and_time("Not sorted", "Sorted", closest1, closest2, x)