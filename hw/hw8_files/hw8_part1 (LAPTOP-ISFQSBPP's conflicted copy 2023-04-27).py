# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 22:54:26 2022

@author: Yathin Vemula
"""
import json
import Bear
import BerryField
import Tourist


input_file_name = input("Enter the JSON file name for the simulation: ")
print(input_file_name)

with open(input_file_name) as f:
    data = json.load(f)

field_data = data["berry_field"]
active_bears_data = data["active_bears"]
active_tourists_data = data["active_tourists"]

# Create tourist list
tourist_list = []
for item in active_tourists_data:
    tourist_list.append(Tourist.Tourist(item[0], item[1]))

# Create bear list
bear_list = []
for item in active_bears_data:
    bear_list.append(Bear.Bear(item[0], item[1], item[2]))

# Print everything
berry_field_instance = BerryField.BerryField(field_data, tourist_list, bear_list)
print("\nField has {} berries.".format(berry_field_instance.totalberries()))
print(berry_field_instance)

print("Active Bears:")
for bear in bear_list:
    print(bear)

print("\nActive Tourists:")
for tourist in tourist_list:
    print(tourist)
