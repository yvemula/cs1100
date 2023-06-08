# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:10:24 2022

@author: Yathin Vemula
"""

from Date import Date
month_names = [ '', 'January', 'February', 'March', 'April','May','June','July','August', 'Spetember', 'October', 'November', 'December' ]

def readFile():
    dates_list = []
    with open("birthdays.txt","r") as file:
        while True:
            line = file.readline().strip() 
            if not line: # this means that there is nothing in the line anymore
                break 
            else: 
                year,month,day = line.split()
                date=Date(year=int(year),month = int(month),day=int(day))
                dates_list.append(date)
    return dates_list
if __name__ == "__main__":
    dates_list = readFile()
    oldest = min(dates_list)
    youngest = max(dates_list)
    print("The oldest birthday: ",oldest)
    print("The youngest birthday: ",youngest)
    month_count = [0,0,0,0,0,0,0,0,0,0,0,0,0] # 13 zeroes since there are 13 namesin month names
    for date in dates_list:# using month_names, we can insert date.month as index which is a number
      month = month_names[date.month]
      index = month_names.index(month) # get the index of the month in themonth_names
      month_count[index] += 1 # add 1 to the count at the specified index
    index_max_month_count = month_count.index(max(month_count))
    max_month = month_names[index_max_month_count]
    print("Month with most birthdays:",max_month)