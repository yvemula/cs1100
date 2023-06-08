# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:19:50 2022

@author: Yathin Vemula
"""

from Ball import *
import tkinter as tk
import random
if __name__ == "__main__":
 #n = int(raw_input("Enter the number of balls you want ==> "))
 root = tk.Tk()
 root.title("Lab 1")
 maxx = 400
 maxy = 400
 wait_time = 90
 count = 0
 chart_1 = tk.Canvas(root, width = maxx, height = maxy, background = "white")
 chart_1.grid(row=0, column=0)
 chart_1.pack()
 colorList = ["blue", "red", "green", "yellow", "magenta", "orange"]
 ball = []
 for i in range(0, 10):
     one_ball = Ball(random.randint(10,390), random.randint(10,390), 
random.randint(-8,8), random.randint(-8,8), random.randint(5,10), 
random.choice(colorList))
     ball.append(one_ball)
 while True:
 
  chart_1.delete(tk.ALL)
  for i in range(0, 10):
         bounding_box = ball[i].bounding_box()
         chart_1.create_oval(bounding_box, fill = ball[i].get_color())
         chart_1.update()
  chart_1.after(wait_time)
  for j in range(0, 10):
         ball[j].move()
         ball[j].check_and_reverse(maxx, maxy)
 #count += 1
 root.mainloop()