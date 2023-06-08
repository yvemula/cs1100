# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:22:19 2022

@author: Yathin Vemula
"""
z=0
input_txt = str(input("Enter the scores file: ")).strip()
print(input_txt)
input_out = str(input("Enter the output file: ")).strip()
print(input_out)
lis=[]
f=open(input_txt)
f_out = open(input_out,"w")
for line in f:
   lis.append(int(line))
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]>lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
while z<len(lis): 
    space = ""        
    for x in lis:
        if x<10:
            space = "   "
        elif x>=100:
            space = " "
        else:
            space = "  "
        if z<10:
            space1 = " "
        else:
            space1 = ""
            
        
        f_out.write(space1+str(z)+":"+space+str(x)+"\n")
        z+=1

f_out.close()
