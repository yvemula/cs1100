# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:35:01 2022

@author: Yathin Vemula
"""
import hw4_util
from re import compile
hw4_util.part1_get_top()
#user input for password
input_password = input("Enter a password => ")
print(input_password)
#function that checks if the length is good, returns a score based on length
def length(password):
    score = 0
    score_str = ""
    password= str(password)
    if(len(password) == 6) or (len(password) == 7):
        score+=1
    elif(8<=len(password)<=10):
        score+=2
    elif(len(password)>10):
        score+=3
    return score
#a function that checks the cases in the user password, based on cases, it will return a certain score
def case(password):
    count1 = 0
    count2 = 0
    score = 0
    password = str(password)
    for x in password:
        if x.isupper():
            count1+=1
        elif x.islower():
            count2+=1
    if count1>=2 and count2>=2:
        score+=2
    elif count1==1 and count2==1:
        score+=1
    elif count1==1 or count2==1:
        score+=1    
    return score
#a function to see if there are numbers in the password, returns a score based on whats found
def digits(password):
    count = 0 
    score = 0
    for x in password:
        if x.isdigit():
            count+=1
    if count>=2:
        score+=2
    elif count == 1:
        score+=1
    return score
#a function that looks for a certian type of puncutation and returns score after found
def punc1(password):
    score1 = 0
    score2 = 0
    score=0
    if password.__contains__("!") or password.__contains__("@") or password.__contains__("#") or password.__contains__("$")  :
        score1+=1
    if score1>0:
        score+=score1
    if score2>0:
        score+=score2   
    return score
#another function that looks for certain puncutation
def punc2(password):
    score =0
    if password.__contains__("%") or password.__contains__("^") or password.__contains__("&") or password.__contains__("*"):
        score+=1
    return score
#checks to see if the password looks like a NYlicense and returns a score based on that check
def NYLicense(password):
    count = 0
    password = str(password)
    plate_format =compile('^[a-zA-Z]{3}[0-9]{4}$')
    if len(password) >= 7:
        if plate_format.match(password):
            count-=2
    return count
#checks a list of common passwords to see if the password is used a lot, returns a score after checked
def common(password):
    score = 0
    common_list = hw4_util.part1_get_top()
    for c in common_list:
        if password.lower()==c:
            score-=3
    return score
#set variables equal to different score(different function calls)
l1 = length(input_password)
c1 = case(input_password)
d1 = digits(input_password)
p1 = punc1(input_password)
p2 = punc2(input_password)
n1 = NYLicense(input_password)
c12 = common(input_password)
#keep a universal score

total_score = 0
#checks if the variables have value and if they do we can print the score and the elements that the password contains
if l1!=0:
    print("Length: +",l1,sep="")
    total_score+=l1
if c1!=0:
    print("Cases: +",c1,sep="")
    total_score+=c1
if d1!=0:
    print("Digits: +",d1,sep="")
    total_score+=d1
if p1!=0:
    print("!@#$: +",p1,sep="")
    total_score+=p1
if p2!=0:
    print("%^&*: +",p2,sep="")
    total_score+=p2
if n1!=0:
    print("License: -2")
    total_score+=-2
if c12!=0:
    print("Common: -3")
    total_score+=-3
#prunt the final score and decide how good the password is based on the combined score
print("Combined score:",total_score)
if total_score <=0:
    print("Password is rejected")
if 1<=total_score <=2:
    print("Password is poor")
if 3<=total_score <=4:
    print("Password is fair")
if 5<=total_score <=6:
    print("Password is good")
if total_score >=7:
    print("Password is excellent")



    