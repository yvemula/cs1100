# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:03:55 2022

@author: Yathin Vemula
"""


def get_words(myfile):
    myfile=open(myfile, encoding='utf8')
    myfile=myfile.read()
    myfile=myfile.replace('|',' ')
    myfile=myfile.lower()
    for i in range(len(myfile)):
        myfile=myfile.replace(',',' ')
        myfile=myfile.replace('.',' ')
    myfile=myfile.split()
    words=set()
    for i in range(len(myfile)):
        if myfile[i].isalpha():
            if len(myfile[i])>=4:
                words.add(myfile[i])
    print(len(words),'words')
    print(words)

if __name__=='__main__':
    myfile=input('Input your file ==> ').strip()
    print("File", myfile)
    get_words(myfile)