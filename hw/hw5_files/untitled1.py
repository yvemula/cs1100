# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:21:19 2022

@author: Yathin Vemula
"""

import hw5_util
def getN(a,rl,cl):

 nu = -1
 nd = -1
 nr = -1
 nl = -1
 if a[0] + 1 < rl:
     nu = (a[0]+1,a[1])
 if a[0] - 1 >= 0:
     nd = (a[0]-1,a[1])
 if a[1] + 1 < cl:
     nr = (a[0],a[1]+1)
 if a[1] - 1 >= 0:
     nl = (a[0],a[1]-1)
 lis = [str(nd),str(nl),str(nr),str(nu)]
 liss= []
 for x in lis:
     if x != '-1':
         liss.append(x)
 return liss
#we take the input of the starting location and the row limit and column limit. We calculute the row up row down column left column right.
#Add to the list and delete those which returns -1

input_n = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
print(input_n)
while input_n > 3:
 input_n = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
 print(input_n)
if input_n == 0:# end the program
 pass
else:
 r = 0
 r1 = True
 d1 = 0
 u1 = 0
 d = input("Should the grid be printed (Y or N): ")
 print(d)
 if d == 'y' or d == 'Y':
     print('Grid {}'.format(input_n))
 for y in hw5_util.get_grid(input_n):
     for x in range(len(y)-1):
         print(str(y[x]).rjust(4),end="")#string formating using rJust
     print(str(y[-1]).rjust(4))
 """rjust can make sure the space when output the string, end= can make 
sure they are print in one line"""
 rl = len(hw5_util.get_grid(input_n))#row limit
 cl = len(hw5_util.get_grid(input_n)[0])#column limit
 print("Grid has {} rows and {} columns".format(len(hw5_util.get_grid(input_n)),len(hw5_util.get_grid(input_n)[0])))
 sl = hw5_util.get_start_locations(input_n)
 for i in sl:
     print("Neighbors of {}: {}".format(i,' '.join(getN(i,rl,cl))))
 for i in range(len(hw5_util.get_path(input_n)) - 1):
     r += 1
     if hw5_util.get_path(input_n)[i][0] != hw5_util.get_path(input_n)[i + 1][0] and hw5_util.get_path(input_n)[i][1] != hw5_util.get_path(input_n)[i + 1][1]:
         r1 = False
         break
     if (hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i + 1][0]][hw5_util.get_path(input_n)[i + 1][1]] - hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i][0]][hw5_util.get_path(input_n)[i][1]]) > 0:#calcute difference and then compare
         u1 += (hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i + 1][0]][hw5_util.get_path(input_n)[i + 1][1]] - hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i][0]][hw5_util.get_path(input_n)[i][1]])
     if (hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i + 1][0]][hw5_util.get_path(input_n)[i + 1][1]] - hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i][0]][hw5_util.get_path(input_n)[i][1]]) < 0:
         d1 = d1 - (hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i + 1][0]][hw5_util.get_path(input_n)[i + 1][1]] - hw5_util.get_grid(input_n)[hw5_util.get_path(input_n)[i][0]][hw5_util.get_path(input_n)[i][1]])
 if r1 == False:
     print('Path: invalid step from {} to {}'.format(hw5_util.get_path(input_n)[r-1],hw5_util.get_path(input_n)[r]))
 if r1 == True:
     print('Valid path')
     print('Downward ' + str(d1))
     print('Upward ' + str(u1))
