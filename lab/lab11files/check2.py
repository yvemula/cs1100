# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:15:19 2022

@author: Yathin Vemula
"""

from tkinter import *
import Ball

    
class BallDraw(object):
    def __init__ (self, parent):
        
        self.b = Ball.Ball(100,150,20,-15,10,'red')
    
       
        self.wait_time = 100 

        
        self.isstopped = False 

        self.maxx = 400 # canvas width, in pixels
        self.maxy = 400 # canvas height, in pixels

        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", \
                             width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)

    def faster(self):
        if self.wait_time > 2:
            self.wait_time //= 2

    def slower(self):
        self.wait_time *= 2
            
    def restart(self):
        self.isstopped = False
        self.b.x,self.b.y = 80,200
        self.animate()
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
        
    def draw_ball(self):
        self.canvas.delete("all")
        
        self.canvas.create_oval(self.b.bounding_box(), fill=self.b.color)
        self.canvas.update()      
        self.canvas.after(self.wait_time)

    def animate(self):
     while not self.isstopped:
    
            self.draw_ball()
            self.b.check_and_reverse(self.maxx, self.maxy)
            self.b.move()


if __name__ == "__main__":
   
    root = Tk()
    root.title("Tkinter: Lab 11")

   
    bd = BallDraw(root)

    
    bd.animate()

  
    root.mainloop()