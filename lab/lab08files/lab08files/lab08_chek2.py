# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:05:50 2022

@author: Yathin Vemula
"""

def get_words(myfile):
    myfile=open(myfile, encoding='utf8')
    line = myfile.read()
    line = line.split("|")
    line = line[1]
    line = line.replace(".", "")
    line = line.replace(",", "")
    line = line.replace('"', "")
    line = line.lower()
    line = line.split()
    s = set()
    for word in line:
        if len(word) >=4 and word.isalpha():
            s.add(word)
    result = s
    print(len(result))
    return result

if __name__=='__main__':
    myfile=input('Please enter file 1 to compare ==> ').strip()
    print(myfile)
    s1 = get_words(myfile)
    myfile2=input('Please enter file 2 to compare ==> ').strip()
    print(myfile)
    s2 = get_words(myfile2)
    print()
    print("Comparing clubs {} and {}".format(myfile,myfile2))
    print()
    print("Same words: ", s1.intersection(s2))
    print()
    print("Unique to", myfile, s1.difference(s2))
    print()
    print("Unique to", myfile2, s2.difference(s1))