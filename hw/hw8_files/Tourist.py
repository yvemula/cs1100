# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:22:03 2022

@author: Yathin Vemula
"""
class Tourist:
    def __init__(self,r,c):
        self.r = r
        self.c = c
        self.die = False
        self.left = False
        self.bored = False
        self.turns = 0
        self.scared = False
    #prints tourist 
    def __str__(self):
        stri = "Tourist at ({},{}), {} turns without seeing a bear.".format(str(self.r),str(self.c),str(self.turns))               
        return stri
    #looks around for any bears
    def sees(self,be):
        count = 0
        belen= len(be)
        for b in range(belen):#calc given
            x = abs(be[b].r - self.r)
            y = abs(be[b].c - self.c)
            x1 = x**2
            y1 = y**2
            if (x1 + y1)**(1/2) <= 4:
                count += 1
        return count