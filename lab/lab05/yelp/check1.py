# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:05:32 2022

@author: Yathin Vemula
"""
import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')
user_id = int(input("Pick a Restaurant: "))
if user_id>len(restaurants):
    print("You've picked no restaurant with that ID")

def print_info(listr,user_id):
    ids= user_id-1
    name = listr[ids].pop(0)
    typeP = listr[ids].pop(4)
    address = listr[ids].pop(2)
    address_list = address.split("+")
    addy =address_list[1].split()
    
    avg_score = listr[ids].pop(3)
    avg = 0
    '''
    for x in avg_score:
        suma += avg_score[x]
    avg = float(suma/len(address_list))
    split_city = str(address_list[2]).split("+")
    '''
    print(name,"("+typeP+")\n\t",address_list[0],"\n\t",addy[0],addy[1],addy[2])
     
    
    for x in range(len(avg_score)):
        avg += avg_score[x]
    avg = float(avg/len(avg_score))
    print("Average score: {:.2f}".format(avg))
    if 0<=avg<=2:
        print("This restaurant is rated bad, based on",len(avg_score),"reviews.")
    elif 2<avg<=3:
        print("This restaurant is rated average, based on",len(avg_score),"reviews.")
    elif 3<avg<=4:
        print("This restaurant is rated above average, based on",len(avg_score),"reviews.")
    elif 4<avg<=5:
        print("This restaurant is rated very good, based on",len(avg_score),"reviews.")
    return ""

print(print_info(restaurants,user_id))
        

