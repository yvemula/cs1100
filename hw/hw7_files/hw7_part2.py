# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:28:34 2022

@author: Yathin Vemula
"""
import json
year = int(input('Min year => '))
print(year)
year_max = int(input('Max year => '))
print(year_max)
weight = input('Weight for IMDB => ')
weight1 = float(weight)
print(weight)
weight2 = float(input('Weight for Twitter => '))
print(weight2)
print('')
weight3 = float(weight2)
if __name__ == '__main__':
 movie_list = list()
 rating_dict = dict()
 input_genre = input('What genre do you want to see? ')
 print(input_genre)
 input_genre = input_genre.title()#has to be captilize
 for i in json.loads(open("movies.json").read()):
     if i in json.loads(open("ratings.json").read()) and len(json.loads(open("ratings.json").read())[i]) >= 3:#have to be in twitter rate and 
         if year <= json.loads(open("movies.json").read())[i]['movie_year'] <= year_max:
             movie_list.append(i)
 while input_genre != 'Stop':#stop while print stop
     for i in movie_list:
             if input_genre in json.loads(open("movies.json").read())[i]['genre']:#only when have the genre
                 rating_dict[i] =  (weight1 * json.loads(open("movies.json").read())[i]['rating'] + weight3 * sum(json.loads(open("ratings.json").read())[i]) /len(json.loads(open("ratings.json").read())[i])) / (weight1+weight3)#adding element into the dictionary
     if len(rating_dict) != 0:
         rating_list =sorted(rating_dict.items(),key = lambda x:x[1])#sort  
         b = rating_list[-1][0]#returns best
         w = rating_list[0][0]#returns worst
         print('\nBest:\n Released in {}, {} has a rating of {:.2f}'.format(json.loads(open("movies.json").read())[b]['movie_year'],json.loads(open("movies.json").read())[b]['name'],rating_list[-1][1]))
         print('\nWorst:\n Released in {}, {} has a rating of {:.2f}'.format(json.loads(open("movies.json").read())[w]['movie_year'],json.loads(open("movies.json").read())[w]['name'],rating_list[0][1]))
     if len(rating_dict) == 0:#if there is no this genre
         print('\nNo {} movie found in {} through {}'.format(input_genre,year,year_max))
         rating_dict.clear()#clear for next loop
         input_genre = input('\nWhat genre do you want to see? ')
         print(input_genre)
         genre=input_genre.title()    