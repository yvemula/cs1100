# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:24:30 2022

@author: Yathin Vemula
"""

from Restaurant import Restaurant

def convert_input_to_restaurant(line):
    '''
    Parse the Yelp input data to create a Restaurant object.
    '''
    m = line.strip().split("|")
    name = m[0]
    latitude = float(m[1])
    longitude = float(m[2])
    address = m[3].split('+')   # creates a list of the address lines
    url = m[4]
    restaurant_type = m[5]
    reviews = []
    for r in m[6:]:
        reviews.append(int(r))
    return Restaurant(name, latitude, longitude, address, url, \
                          restaurant_type, reviews )

def build_restaurant_list( file_name ):
    '''
    Assuming the Yelp data is in the form of one line per restaurant,
    read each line, create a restaurant object from each, and form a
    list of these objects.  Return the list.
    '''
    restaurants = []
    for line in open(file_name):
        restaurants.append(convert_input_to_restaurant(line))
    return restaurants
   
if __name__ == "__main__":
    file_name = 'yelp.txt'
    restaurants = build_restaurant_list( file_name )
    num_restaurants = len(restaurants)
    city = "Troy"
    List = []
   
    top_name = ''
   
    for x in restaurants:
        if not x.is_in_city(city):
            continue

    # Initial code to print the first three restaurants, just to see
    # how each restaurant is formed into an object and converted to a
    # string for output.
       
        if 'American' in x.category:
            rating = x.average_review()
            if float(rating) > 3.00:
                top_name = x.name
                List.append(top_name)
   
    List=sorted(List)
    for i in List:
        print(i)

   