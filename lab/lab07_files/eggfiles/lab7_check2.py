# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:01:51 2022

@author: Yathin Vemula
"""

def isinteger(inputstr):
    try:
        value=int(inputstr)
        return True
    except ValueError:
        return False

def parse_line(input_string):
    splitstr=input_string.split('/')
    if(isinteger(splitstr[0])) and isinteger(splitstr[1]) and isinteger(splitstr[2]):
        rep=(splitstr[0], splitstr[1], splitstr[2], splitstr[3] +"/"+splitstr[4])
        print(rep)
    else:
        print("None")

def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i+1

def get_line(fname, parno, lineno):
    paragraphs=1
    your_line_num=0
    previous=[]
    with open(str(fname)+'.txt','r') as file:
        for line in file:
            previous.append(line)
            line.strip()
            if line == '\n' or previous[-1:]=='\n':
                paragraphs+=1
                your_line_num=0
            if line!='\n':
                paragraphs=paragraphs
                your_line_num+=1
            if paragraphs==parno:
                if your_line_num==lineno:
                    return line.strip()

filename=int(input("Please file number ==> "))
paragraphs=int(input("Please enter the line number ==> "))
line=int(input("Please enter the line number ==> "))

print(get_line(filename, paragraphs, line))
