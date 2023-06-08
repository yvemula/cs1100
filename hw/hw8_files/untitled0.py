# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:32:31 2022

@author: Yathin Vemula
"""

class BerryField:
    def __init__(self, berry_field, active_bears, reserve_bears, active_tourists,reserve_tourists):
        self.board = berry_field
        self.active_bears = active_bears
        self.reserve_bears = reserve_bears
        self.active_tourists = active_tourists
        self.reserve_tourists = reserve_tourists
    def get_berries_count(self):
        count = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                count += self.board[r][c]
        return count
    def step(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] >= 1 and self.board[r][c] < 10:
                    self.board[r][c] += 1
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    grow = False
                    if r > 0 and self.board[r - 1][c] == 10:
                        grow = True
                    if r < len(self.board) - 1 and self.board[r + 1][c] == 10:
                        grow = True
                    if c > 0 and self.board[r][c - 1] == 10:
                        grow = True
                    if c < len(self.board) - 1 and self.board[r][c + 1] == 10:
                        grow = True
                    if grow:
                        self.board[r][c] = 1
    def __str__(self):
         s = 'Field has {} berries.\n'.format(self.get_berries_count())
         board = []
         for r in range(len(self.board)):
             rows = []
             for c in range(len(self.board[r])):
                 rows.append(self.board[r][c])
             board.append(rows)
         for active_tourist in self.active_tourists:
          if board[active_tourist.row][active_tourist.col] == 'T':
                 board[active_bear.row][active_bear.col] = 'X'
                 active_bear.asleep = 3
          else:
             board[active_bear.row][active_bear.col] = 'B'
         for r in range(len(board)):
             for c in range(len(board[r])):
                 s += '{:>4}'.format(board[r][c])
             s += '\n'
         s += '\nActive Bears:\n'
         for active_bear in self.active_bears:
             s += str(active_bear) + '\n's += '\nActive Tourists:\n'for active_tourist in self.active_tourists:s += str(active_tourist) + '\n'return sdef next_turn(self):self.update_tourist()self.update_berry()self.update_bear()self.update_tourist2()def update_tourist(self):tourists = []for active_tourist in self.active_tourists:left = Falsecount = 0for active_bear in self.active_bears:if active_bear.row == active_tourist.row and active_bear.col ==active_tourist.col:left = Trueif active_bear.get_distance(active_tourist.row, active_tourist.col)<= 4:count += 1if left or count >= 3:tourists.append(active_tourist)print('{} - Left the Field'.format(active_tourist))if count == 0 and active_tourist.turns == 2:tourists.append(active_tourist)print('{} - Left the Field'.format(active_tourist))for tourist in tourists:self.active_tourists.remove(tourist)def update_tourist2(self):tourists = []for active_tourist in self.active_tourists:left = Falsecount = 0for active_bear in self.active_bears:if active_bear.row == active_tourist.row and active_bear.col ==active_tourist.col:left = Trueif active_bear.get_distance(active_tourist.row, active_tourist.col)<= 4:count += 1if left or count >= 3:tourists.append(active_tourist)

             