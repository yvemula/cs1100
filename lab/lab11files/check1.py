# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:11:58 2022

@author: Yathin Vemula
"""

from tkinter import *

class Ball(object):
    def __init__ (self,x,y,dx,dy,radius,color):
        self.x,self.y = x,y
        self.radius = radius
        self.dx,self.dy = dx,dy
        self.color = color
        self.isstopped = False 
        
    def position(self):
        return self.x,self.y

    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def bounding_box(self):
        bounding_box = (self.x-self.radius, \
                        self.y-self.radius,\
                        self.x+self.radius, \
                        self.y+self.radius)         
        return bounding_box
        
    def get_color(self):
        return self.color
        
    def some_inside(self,maxx,maxy):
        if 0 < self.x + self.radius and \
              self.x - self.radius < maxx and \
              0 < self.y + self.radius and \
              self.y - self.radius < maxy:     
            return True
        return False
    
class BallDraw(object):
    def __init__ (self, parent):
        
        self.b = Ball(100,150,20,-15,10,'red')
    
       
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
        
        # Draw an oval on the canvas within the bounding box
        self.canvas.create_oval(self.b.bounding_box(), fill=self.b.color)
        self.canvas.update()      # Actually refresh the drawing on the canvas.

   
        self.canvas.after(self.wait_time)

    def animate(self):
        ##  Loop until the ball runs off the screen.
        while 0 < self.b.x + self.b.radius and \
              self.b.x - self.b.radius < self.maxx and \
              0 < self.b.y + self.b.radius and \
              self.b.y - self.b.radius < self.maxy and \
              not self.isstopped:
            # Move the ball
            self.draw_ball()
            self.b.x += self.b.dx
            self.b.y += self.b.dy


if __name__ == "__main__":
   
    root = Tk()
    root.title("Tkinter: Lab 11")

    ## Create a class to handle all our animation
    bd = BallDraw(root)

    ## Run the animation by continuously drawing the ball and then moving it
    bd.animate()


    root.mainloop()
