# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:45:23 2022

@author: Yathin Vemula
"""

def find_min(lis):
    min_lis = []
    for x in lis:
        min_lis.append(min(x))
    m1 = min(min_lis)
    return m1
if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )