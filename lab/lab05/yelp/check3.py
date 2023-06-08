# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:06:40 2022

@author: Yathin Vemula
"""

import lab05_util,webbrowser

restaurants = lab05_util.read_yelp('yelp.txt')
user_id = int(input("Pick a Restaurant: "))
if user_id>len(restaurants):
    print("You've picked no restaurant with that ID")

def print_info(listr,user_id):
    ids= user_id-1
    name = listr[ids][0]
    typeP = listr[ids][5]
    address = listr[ids][3]
    address_list = address.split("+")
    addy =address_list[1].split()
    
    
    avg_score = listr[ids][6]
    avg = 0
 
    website = listr[ids].pop()
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
    return "\n"

print(print_info(restaurants,user_id))
print("What would you like to do next?\n1. Visit the homepage\n2. Show on Google Maps\n3. Show directions to this restaurant")
user_choice = int(input("Your choice (1-3)? ==>"))


def websites(listr,user_id):
    ids= user_id-1

    address = listr[ids][3]
    address_list = address.split("+")
    addy =address_list[1].split()
    
 
    website = listr[ids][4]
    if user_id == 1:
        webbrowser.open(website)
    elif user_id==2:
        webbrowser.open('http://www.google.com/maps/place/'+address_list[0]+'-'+addy[0]+'-'+addy[1]+'-'+addy[2])
    elif user_id == 3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/'+address_list[0]+" "+addy[0]+" "+addy[1]+" "+addy[2])
websites(restaurants, user_choice)
