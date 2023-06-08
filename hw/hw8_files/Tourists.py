# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:22:03 2022

@author: Yathin Vemula
"""
class Tourist:     
    def __init__(self,r,c):  
        self.r = r        
        self.c = c   
        self.turns = 0  
        self.die = False    
        self.scared = False 
        self.left = False   
        self.bored = False     #prints tourist
    def __str__(self):     
        string = "Tourist at ({},{}), {} turns without seeing a bear.".format(str(self.r),str(self.c),str(self.turns))
        return string     #looks around for any bears
    def sees(self,bears):  
        counter = 0    
        for b in range(len(bears)):  
            x = abs(bears[b].r - self.r)  
            y = abs(bears[b].c - self.c)             
            xsq = x**2    
            ysq = y**2       
        if (xsq + ysq)**.5 <= 4:       
            counter += 1   
        return counter