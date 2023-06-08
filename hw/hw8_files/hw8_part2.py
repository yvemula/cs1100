# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:39:43 2022

@author: Yathin Vemula
"""
import json
import BerryField
import Bear
import Tourist
 
json_filename = input("Enter the json file name for the simulation => ")
print(json_filename)

with open(json_filename) as f:
    data = json.load(f)

field_data = data["berry_field"]
active_bears_data = data["active_bears"]
reserve_bears_data = data["reserve_bears"]
active_tourists_data = data["active_tourists"]
reserve_tourists_data = data["reserve_tourists"]

tourist_list = []
tourist_count = len(active_tourists_data)

for i in range(tourist_count):
    tourist_list.append(Tourist.Tourist(active_tourists_data[i][0], active_tourists_data[i][1]))

bear_list = []
active_bear_count = len(active_bears_data)

for i in range(active_bear_count):
    bear_list.append(Bear.Bear(active_bears_data[i][0], active_bears_data[i][1], active_bears_data[i][2]))

print("\nStarting Configuration")

berry_field = BerryField.BerryField(field_data, tourist_list, bear_list)
print("Field has {} berries.".format(berry_field.totalb()))
print(berry_field)
print("Active Bears:")

bear_list_length = len(bear_list)
tourist_list_length = len(tourist_list)

for i in range(bear_list_length):
    print(bear_list[i])

print("\nActive Tourists:")
for i in range(tourist_list_length):
    print(tourist_list[i])

turn = 1
while True:
    if turn == 1:
        print("\nTurn: {}".format(turn))
    else:
        print("\n\nTurn: {}".format(turn))

    berry_field.growb()
    berry_field.spreadb()

    for b in range(bear_list_length):
        for t in range(tourist_list_length):
            if bear_list[b].r == tourist_list[t].r and bear_list[b].c == tourist_list[t].c:
                bear_list[b].kill = True
                tourist_list[t].die = True

    removal_count = 0
    for t in range(tourist_list_length):
        if tourist_list[t - removal_count].scared == True or tourist_list[t - removal_count].die == True:
            print("{} - Left the Field".format(tourist_list[t - removal_count]))
            tourist_list.remove(tourist_list[t - removal_count])
            removal_count += 1

    for b in range(bear_list_length):
        if bear_list[b].sleep == True:
            bear_list[b].turns -= 1
        if bear_list[b].turns == 0:
            bear_list[b].sleep = False
        if bear_list[b].kill == True:
            bear_list[b].kill = False
            bear_list[b].sleep = True
            bear_list[b].turns = 4

        if bear_list[b].left == False and bear_list[b].sleep == False:
            while True:
                bear_list[b].eat += berry_field.field[bear_list[b].r][bear_list[b].c]
                berry_field.field[bear_list[b].r][bear_list[b].c] = 0
                bear_list[b].move()

                for t in range(tourist_list_length):
                    if bear_list[b].c == tourist_list[t].c and bear_list[b].r == tourist_list[t].r:
                        bear_list[b].kill = True
                        tourist_list[t].die = True

                if bear_list[b].r > len(berry_field.field) - 1:
                    bear_list[b].left = True
                    break
                if bear_list[b].kill == True:
                    break
                elif bear_list[b].r < 0:
                    bear_list[b].left = True
                    break
                elif bear_list[b].c > len(berry_field.field) - 1:
                    bear_list[b].left = True
                    break
                elif bear_list[b].c < 0:
                    bear_list[b].left = True
                    break

                bear_list[b].eat += berry_field.field[bear_list[b].r][bear_list[b].c]
                berry_field.field[bear_list[b].r][bear_list[b].c] = 0

                if bear_list[b].eat >= 30:
                    berry_field.field[bear_list[b].r][bear_list[b].c] = bear_list[b].eat - 30
                    break

        bear_list[b].eat = 0

    turn += 1


  
     #sees if a bear eats a tourist
    for b in range(bear_list_length):
        for t in range(tourist_list_length):
            if bear_list[b].r == tourist_list[t].r and bear_list[b].c == tourist_list[t].c:
                tourist_list[t].die = True
                bear_list[b].kill = True
    
    for t in range(len(tourist_list)):
        if tourist_list[t].die == False:
            if tourist_list[t].sees(bear_list) >= 3:
                tourist_list[t].scared = True
            if tourist_list[t].sees(bear_list) > 0:
                tourist_list[t].turns = 0
            if tourist_list[t].sees(bear_list) == 0:
                tourist_list[t].turns += 1
    
    for t in range(tourist_list_length):
        if tourist_list[t].turns == 3:
            tourist_list[t].bored = True
    
    for b in range(bear_list_length):
        if bear_list[b].kill == True:
            bear_list[b].sleep = True
            bear_list[b].turns = 3
            bear_list[b].kill = False
    
    for t in range(tourist_list_length):
        if tourist_list[t].sees(bear_list) >= 3:
            tourist_list[t].scared = True
    
    removal_counter = 0
    for t in range(len(tourist_list)):
        if tourist_list[t - removal_counter].die == True or tourist_list[t - removal_counter].scared == True or tourist_list[t - removal_counter].bored == True:
            print("{} - Left the Field".format(tourist_list[t - removal_counter]))
            tourist_list.remove(tourist_list[t - removal_counter])
            removal_counter += 1
    
    bear_removal_counter = 0
    for b in range(len(bear_list)):
        if bear_list[b - bear_removal_counter].left == True:
            print("{} - Left the Field".format(bear_list[b - bear_removal_counter]))
            bear_list.remove(bear_list[b - bear_removal_counter])
            bear_removal_counter += 1
    
    print("Field has {} berries.".format(berry_field.totalb()))
    print(berry_field)
    print("Active Bears:")
    for bear in range(len(bear_list)):
        if bear_list[bear].sleep == True and bear_list[bear].turns - 1 > 0:
            print("{} - Asleep for {} more turns".format(bear_list[bear], (bear_list[bear].turns - 1)))
        else:
            print(bear_list[bear])
    
    print("\nActive Tourists:")
    for tourist in range(len(tourist_list)):
        print(tourist_list[tourist])
    
    turn += 1
    if turn == 6:
        break
print()

