# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:22:03 2022

@author: Yathin Vemula
"""
class Tourist:
    def init(self, row, col):
        self.row = row
        self.col = col
        self.is_dead = False
        self.has_left = False
        self.is_bored = False
        self.turn_count = 0
        self.is_scared = False
    def __str__(self):
        description = "Tourist at ({},{}), {} turns without seeing a bear.".format(
            str(self.row), str(self.col), str(self.turn_count))
        return description
    
    def sees(self, bears):
        nearby_bears = 0
        num_bears = len(bears)
        for idx in range(num_bears):
            delta_row = abs(bears[idx].row - self.row)
            delta_col = abs(bears[idx].col - self.col)
            squared_row = delta_row**2
            squared_col = delta_col**2
            if (squared_row + squared_col)**(1/2) <= 4:
                nearby_bears += 1
        return nearby_bears