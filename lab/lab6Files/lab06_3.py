# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:09:02 2022

@author: Yathin Vemula
"""
import lab06_util
bd=[['1','.','.','.','2','.','.','3','7'],
    ['.','6','.','.','.','5','1','4','.'],
    ['.','5','.','.','.','.','.','2','9'],
    ['.','.','.','9','.','.','4','.','.'],
    ['.','.','4','1','.','3','7','.','.'],
    ['.','.','1','.','.','4','.','.','.'],
    ['4','3','.','.','.','.','.','1','.'],
    ['.','1','7','5','.','.','.','8','.'],
    ['2','8','.','.','4','.','.','.','6']]

print(len(bd))
print(len(bd[0]))
print(bd[0][0])
print(bd[8][8])


for i in range(0,len(bd)):
    a="-------------------------"
    print(a)
    a="|"
    for j in range(0,len(bd[0])):
        a=a+' ' 
        a=a+bd[i][j]
        if j%3==0 and j!=0:
            a=a+' '
            a=a+'|'
    a=a+' '
    a=a+'|'
    print(a)
    if i+1==len(bd):
        a="-------------------------"
        print(a)
def ok_to_add(row,col,val):
 if (row > 9) or (row < 0):
     print("Not valid")
 elif (col > 9) or (col < 0):
     print("Not valid")
 elif (val > 9) or (val < 0):
     print("Not valid") 
 b_row = (row // 3) * 3
 b_col = (col // 3) * 3
 
 for i in range(b_row, b_row + 3):
     for j in range(b_col, b_col +3):
         if bd[i][j] == str(val):
            return False
 for i in range(len(bd[row])):
     if bd[row][i] == str(val):
         return False
 for i in range(len(bd)):
     if bd[i][col] == str(val):
         return False
 bd[row][col] = val
 return True
def verify_board():
    for i in range(9):
        for j in range(9):
            if bd[i][j] == '.':
                return False
            elif ok_to_add(i,j,int(bd[i][j])) == False:
                return False
    return True
            
            
filename = input('Enter a file name ==> ')
bd = lab06_util.read_sudoku(filename)
for i in range(len(bd)):
    l='|'
    for j in range(len(bd[i])):
        l=l+' '+bd[i][j]+' '
        if j%3==2:
            l+='|'
 
    if i%3==0:
        print('-'*len(l))
    print(l)
print('-'*len(l))
i=lab06_util.read_sudoku(filename)
list1=[]
won = False
for row in i:
    if row.count('.')!=0:
        list1.append('1')
if len(list1)==0:
 print('Board is finished!')
 print("You Win!")
 
else:
    while verify_board()==False:
        row=int( input('Enter a row number ==> '))
        column= int( input('Enter a column number ==> '))
        number= int( input('Enter a number to assign ==> '))
        if ok_to_add(row,column,number) == False:
            print("This number cannot be added")
        else:
            for i in range(len(bd)):
                l = '|'
                for j in range(len(bd[i])):
                    l+=(" "+str(bd[i][j]) + " ")
                    if j%3 == 2:
                        l+="|"
                if i%3 == 0:
                    print("-"*len(l))
                print(l)
            print("-"*len(l))
    