# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:22:01 2022

@author: Yathin Vemula
"""

class Bear:
    def init(self, row, col, direction):
            self.row = row
            self.col = col
            self.direction = direction
            self.is_left = False
            self.num_turns = 0
            self.food = 0
            self.dead = False
            self.asleep = False
    def __str__(self):
        row_str = str(self.row)
        col_str = str(self.col)
        direction_str = str(self.direction)
        bear_str = "Bear at ({},{}) moving {}".format(row_str, col_str, direction_str)
        return bear_str

    def move(self):
        dir = self.direction
        cur_row = self.row
        cur_col = self.col
        if dir == "N":
            cur_row -= 1
        elif dir == "E":
            cur_col += 1
        elif dir == "S":
            cur_row += 1
        elif dir == "W":
            cur_col -= 1
        elif dir == "SW":
            cur_row += 1
            cur_col -= 1
        elif dir == "SE":
            cur_row += 1
            cur_col += 1
        elif dir == "NE":
            cur_row -= 1
            cur_col += 1
        elif dir == "NW":
            cur_row -= 1
            cur_col -= 1

        self.row = cur_row
        self.col = cur_col
 
