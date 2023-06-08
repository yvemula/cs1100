# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:09:13 2022

@author: Yathin Vemula
"""
class BerryField:
    def init(self, grid, visitors, creatures):
        self.grid = grid
        self.creatures = creatures
        self.visitors = visitors
    def __str__(self):
        output = ''
        conflict = False
        creature_present = False
        visitor_present = False
        grid_size = len(self.grid)
        for x in range(grid_size):
            for y in range(grid_size):
                for creature_idx in range(len(self.creatures)):
                    for visitor_idx in range(len(self.visitors)):
                        if (self.creatures[creature_idx].r == x and
                            self.creatures[creature_idx].c == y and
                            self.visitors[visitor_idx].r == x and
                            self.visitors[visitor_idx].c == y):
                            output += "{:>4}".format("X")
                            conflict = True
    
                if not conflict:
                    for creature_idx in range(len(self.creatures)):
                        if self.creatures[creature_idx].r == x and self.creatures[creature_idx].c == y:
                            output += "{:>4}".format("B")
                            creature_present = True
                    for visitor_idx in range(len(self.visitors)):
                        if self.visitors[visitor_idx].r == x and self.visitors[visitor_idx].c == y:
                            output += "{:>4}".format("T")
                            visitor_present = True
    
                if not conflict and not creature_present and not visitor_present:
                    output += "{:>4}".format(self.grid[x][y])
                conflict = False
                creature_present = False
                visitor_present = False
            output += "\n"
        return output
    
    def totalb(self):
        total = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                total += self.grid[row][col]
        return total
    
    def growb(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if 1 <= self.grid[row][col] < 10:
                    self.grid[row][col] += 1
    
    def spreadb(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if self.grid[row][col] == 10:
                    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                                 (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
    
                    for neighbor_row, neighbor_col in neighbors:
                        if 0 <= neighbor_row < len(self.grid) and 0 <= neighbor_col < len(self.grid):
                            if self.grid[neighbor_row][neighbor_col] == 0:
                                self.grid[neighbor_row][neighbor_col] = 1
        
        