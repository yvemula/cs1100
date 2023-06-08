# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:16:51 2022

@author: Yathin Vemula
"""
import string
alphabet = list(string.ascii_lowercase)
def drop(w):#drop function breaks into a list
    list1=[]
    for i in range(len(w)):
        list2=w[0:i]
        list2 = list2+w[i+1:]
        if (list2) in dicti.keys():
            if list2 not in list1:
                list1.append(list2)
    if len(list1) > 0:
        return True
    else:
        return False
def insert(w,a): #adds an alphabet before each letter and uses a sublist to determine loocation
    list1=[]
    for i in range(len(w)):
        for z in range(len(a)):
            list2=w[:i]
            list2=list2+a[z]
            list2 = list2+w[i:]
            if (list2) in dicti.keys():
                if list2 not in list1:
                    new_list.append(list2)
    for i in range(len(a)):
        if w+a[i] in dicti.keys():
            if w+a[i] not in list1:
                list1.append(w+a[i])
    if len(list1) > 0:
        return True#return true if we could find words
    else:
        return False
def swap(w):#swap function if not out of range trhe order is changed
    list1=[]
    for z in range(len(list(w))-1):
        l2=list(w).copy()
        l2[z+1],l2[z]=l2[z],l2[z+1]
        if (''.join(l2)) in dicti.keys():
            if ''.join(l2) not in list1:
                list1.append(''.join(l2))
    if len(list1) > 0:
        return True
    else:
        return False
def replace(w,k):#replace function puts into a dictionary first word as key and other as values
    list1=[]
    new_list1=list(w)
    diction = dicti.keys()
    for i in range(len(list(w))):
        for ke,val in k.items():
            if new_list1[i]==ke:
                for let in range(len(val)):
                    list2=new_list1.copy()
                    list2[i]=val[let]
                    list2=list2.copy()
                    if (''.join(list2)) in diction:
                        if ''.join(list2) not in list1:
                            list1.append(w)
    if len(list1) > 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    #input values
    file1=input("Dictionary file => ").strip()
    print(file1)
    file2=input("Input file => ").strip()
    print(file2)
    file3=input("Keyboard file => ").strip()
    print(file3)
    dicti=dict()
    list1=[]
    keys=dict()
    #we open each file
    with open(file1, 'r') as f:
        for w in f:
            dicti[w.split(',')[0]]=float(w.split(',')[1].strip('\n'))
    with open(file2, 'r') as f:
        in_file=f.read().replace('\n'," ").split()
    for w in in_file:
        list1.append(w)
    with open(file3, 'r') as f:
        for l in f:
            keys[l.strip("\n").split(" ")[0]]=l.strip("\n").split(" ")[1:]
    for w in list1:
        if w in dicti.keys():
            print("{} -> FOUND".format(w.rjust(15)))
        else:
            new_list=[]
            lis1=[]
            lis2=[]
            #checking functions returns with if statements
            if drop(w)==True:
                for i in range(len(w)):
                    if (w[0:i]+w[i+1:]) in dicti.keys():
                        if w[0:i]+w[i+1:] not in new_list:
                            new_list.append(w[0:i]+w[i+1:])
            if insert(w,alphabet)==True:
                for i in range(len(w)):
                    for z in range(len(alphabet)):
                        if (w[:i] + alphabet[z] + w[i:]) in dicti.keys():
                            if w[:i] + alphabet[z] + w[i:] not in new_list:
                                new_list.append(w[:i] + alphabet[z] + w[i:])
                for i in range(len(alphabet)):
                    if w+alphabet[i] in dicti.keys():
                        if w+alphabet[i] not in new_list:
                            new_list.append(w+alphabet[i])
            if swap(w)==True:
                letter=list(w)
                for l in range(len(list(w))-1):
                    new_word=list(w).copy()
                    new_word[l],new_word[l+1]=new_word[l+1],new_word[l]
                    new_list1 = new_word.copy()
                    if (''.join(new_list1)) in dicti.keys():
                        if ''.join(new_list1) not in new_list:
                            new_list.append(''.join(new_list1))
            if replace(w,keys)==True:
                for i in range(len(list(w))):
                    for k,val in keys.items():
                        if list(w)[i]==k:
                            for letters in range(len(val)):
                                new_word=list(w).copy()
                                new_word[i]=val[letters]
                                if (''.join(new_word)) in dicti.keys():
                                    if ''.join(new_word) not in new_list:
                                        new_list.append(''.join(new_word))
           
            for i in new_list:
                
                lis1.append((dicti[i],i))
            lis1.sort(reverse=True)
            for t in lis1:
                lis2.append(t[0+1])
            if len(new_list)>0:
                string=' '.join(str(a) for a in lis2[:3])
                #print lines in the end
                if len(new_list)>=10:
                    print("{} -> FOUND {}:  {}".format(w.rjust(15), len(new_list), string))
                else:
                    print("{} -> FOUND  {}:  {}".format(w.rjust(15), len(new_list), string))
                
            else:
                print("{} -> NOT FOUND".format(w.rjust(15)))
                