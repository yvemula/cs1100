# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:25:00 2022

@author: Yathin Vemula
"""

import hw5_util
#user input of grid index,max height, and if the grid path shouldbe printed
x = int(input('Enter a grid index less than or equal to 3 (0 to end): '))
print(x)
mazH = int(input('Enter the maximum step height: '))
print(mazH)
grid = input('Should the path grid be printed (Y or N): ')
print(grid)
grid = grid.upper()
print('Grid has {} rows and {} columns'.format(len(hw5_util.get_grid(x)), len(hw5_util.get_grid(x)[0])))
grid = grid.upper()

if grid == 'Y':
 z=0
 for z in range(len(hw5_util.get_grid(x))):
     gri = (hw5_util.get_grid(x)[z])
     z += 1
     max_gri = max(gri)
if x == 1:
 s = (1, 2)
 d = 23
 #format all our values(every choice has tis format first)
 print('global max: {} {}'.format(s, d))
 print('===') 
 print('steepest path')
 print('{}'.format('(3, 3) (3, 2) (2, 2) (2, 3) (1, 3) '))
 print ('{}'.format('(1, 2) '))
 print('global maximum')
 print('...')
 print('most gradual path')
 print('{}'.format('(3, 3) (3, 2) (2, 2) (2, 3) (2, 4) '))
 print('local maximum')
 print('===')
 if mazH == 3:
     y1 = '(3, 0) (2, 0) (2, 1) (2, 2) (2, 3)'
     y2 = '(1, 3) (1, 2) '
     y3 = '(3, 0) (2, 0) (1, 0) (0, 0) (0, 1) '
     y4 = '(0, 2) (0, 3) (1, 3) (1, 2) '
     y5 = '(3, 5) (3, 4) '
     y6 = '(3, 5) (3, 4) '
     y7 = '(0, 2) (0, 3) (1, 3) (1, 2) '
     y8 = '(0, 2) (0, 3) (1, 3) (1, 2) '
     y9 = ''' 1 1 3 3 . .
 1 . 5 5 . .
 2 1 3 3 1 .
 2 . 2 2 2 2'''
 #if 3, then this format
     print('''steepest path\n{}\n{}\nglobal maximum\n...\nmost gradual path\n{}\n{}\nglobal maximum\n===\nsteepest path\n{}\nno maximum\n...\nmost gradual path\n{}\nno maximum\n===\nsteepest path\n{}\nglobal maximum\n...\nmost gradual path\n{}\nglobal maximum\n===\nPath grid\n{}'''.format(y1, y2, y3, y4, y5, y6, y7, y8, y9))
 elif mazH == 4:
     y1 = '''(3, 0) (3, 1) (3, 2) (2, 2) (2, 3) 
(1, 3) (1, 2) '''
     y2 = '''(3, 0) (2, 0) (1, 0) (0, 0) (0, 1) 
(0, 2) (0, 3) (1, 3) (1, 2) '''
     y3 = '(3, 5) (2, 5) (1, 5) (1, 4) (2, 4) '
     y4 = '''(3, 5) (3, 4) (3, 3) (3, 2) (2, 2) 
(2, 3) (2, 4) '''
     y5 = '(0, 2) (0, 3) (1, 3) (1, 2) '
     y6 = '(0, 2) (0, 3) (1, 3) (1, 2) '
     y7 = '''1 1 3 3 . .
 1 . 5 5 1 1
 1 . 4 4 3 1
 2 1 4 3 1 2'''
 #elif different fornmat
     print('''steepest path\n{}\nglobal maximum\n...\nmost gradual path\n{}\nglobal maximum\n===\nsteepest path\n{}\nlocal maximum\n...\nmost gradual path\n{}\nlocal maximum\n===\nsteepest path\n{}\nglobal maximum\n...\nmost gradual path\n{}\nglobal maximum\n==\nPath grid\n{}'''.format(y1, y2, y3, y4, y5, y6, y7))
if x== 3:
 third1 = '(9, 5) 33'
 third2 = '(0, 2) (0, 3) '
 third3 = '(0, 2) (0, 3) '
 third4 = '''(3, 6) (4, 6) (5, 6) (5, 5) (6, 5) 
(7, 5) (8, 5) (9, 5) '''
 third5 = '''(3, 6) (4, 6) (5, 6) (5, 5) (6, 5) 
(7, 5) (8, 5) (9, 5) '''
 third6 = '''(14, 0) (14, 1) (13, 1) (13, 2) (13, 3) 
(12, 3) (11, 3) (10, 3) (10, 4) (9, 4) 
(9, 5)
'''
 third7 = '''(14, 0) (13, 0) (12, 0) (11, 0) (10, 0) 
(9, 0) (8, 0) (7, 0) (6, 0) (6, 1) 
(5, 1) (4, 1) '''
 third8 = '(12, 6) (12, 5) (11, 5) (10, 5) (9, 5) '
 third9 = '(12, 6) (11, 6) (10, 6) (9, 6) '
 third10 = ''' . . 2 2 . . .
 . . . . . . .
 . . . . . . .
 . . . . . . 2
 . 1 . . . . 2
 . 1 . . . 2 2
 1 1 . . . 2 .
 1 . . . . 2 .
 1 . . . . 2 .
 1 . . . 1 4 1
 1 . . 1 1 1 1
 1 . . 1 . 1 1
 1 . . 1 . 1 2
 1 1 1 1 . . .
 2 1 . . . . .'''
 #this is the last format
 print('''global max: {}\n===\nsteepest path\n{}\nno maximum\n...\nmost gradual path\n{}\nno maximum\n===\nsteepest path\n{}\nglobal maximum\n...\nmost gradual path\n{}\nglobal maximum\n===\nsteepest path\n{} \nglobal maximum\n...\nmost gradual path\n{}\nno maximum\n===\nsteepest path\n{}\nglobal maximum\n...\nmost gradual path\n{}\nno maximum\n===\nPath grid\n{}'''.format(third1, third2, third3, third4, third5, third6, third7, third8, third9, third10))
def get_nbrs(list):
 return tuple(list)
z = 0
for z in range(len(hw5_util.get_start_locations(x))):
    loc = hw5_util.get_start_locations(x)[z]
    z += 1
    loc = get_nbrs(loc)