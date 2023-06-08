# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 23:07:12 2022

@author: Yathin Vemula
"""

'''
Template program for Lecture 20 exercises.
'''

def linear_search( x, L ):
        if x in L:
            return L.index(x)
        else:
            for i in range(0, len(L)):
                if i == 0 and x < L[i]:
                    return i
                elif i+1 != len(L):
                    if L[i] < x < L[i+1]:
                        return i+1
                elif i+1 == len(L):
                    if x > L[len(L)-1]:
                        return i+1
                    


if __name__ == "__main__":
    #  Get the name of the file containing data
    fname = input('Enter the name of the data file => ')
    print(fname)

    #  Open and read the data values
    in_file = open(fname,'r')
    values = []
    for line in in_file:
        v = float(line)
        values.append(v)

    #  Search for each value requested by the user until -1 is entered
    x = 0
    while x != -1:
        x = float(input("Enter a value to search for ==> "))
        print(x)
        if x != -1:
            loc = linear_search(x, values)
            print(loc)

