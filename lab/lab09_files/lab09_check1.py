# -*- coding: utf-8 -*-
"""
Created on Tue Nov 7 10:20:22 2022

@author: Yathin Vemula
"""
days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 
'July', 'August',\
 'September', 'October', 'November', 'December' ]
 
class Date:
 def __init__(self, year=1900, month=1, day=1):
  self.year=year
  self.month=month
  self.day=day
 
 def __str__(self):
  return "%s/%s/%s" %(self.year, str(self.month).rjust(2, "0"), 
str(self.day).rjust(2, '0'))
 
 def same_day_in_year(self, other):
  if self.month== other.month:
   if self.day == other.day:
    return True 
  else: 
   return False 
#--------------------check 1^ -----------------------
 def is_leap_year(self):
  if self.year%4 != 0:
   return False
  elif self.year%100 and not self.year%400 != 0:
   return False
  else: 
   return True
 
 def __lt__(d1,d2):
  if d1.year > d2.year:
   return False 
  elif d1.year == d2.year and d1.month > d2.month:
   return False 
  elif d1.year == d2.year and d1.month == d2.month and d1.day >= d2.day:
   return False 
  else:
   return True
 
 
 
 
if __name__ == "__main__":
  d1 = Date(1972, 3, 27)
  d2 = Date(1998, 4, 13)
  d3 = Date(1996, 4, 13)
  print ("d1: " + str(d1))
  print ("d2: " + str(d2))
  print ("d3: " + str(d3))
  print ("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
  print ("d2.same_day_in_year(d3)", d2.same_day_in_year(d3) )
 
 #----------------Part 1^-------------------------------------
 
  print ("\nd1.is_leap_year()", d1.is_leap_year())
  print ("d2.is_leap_year()", d2.is_leap_year())
  print ("d1 < d2", d1<d2)
  print ("d2 < d3", d2<d3)
