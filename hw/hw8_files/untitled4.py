# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 23:07:13 2022

@author: Yathin Vemula
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:09:13 2022

@author: Yathin Vemula
"""
class BerryField:
    def __init__(self,berryfield,tourists,bears):
         self.berryfield = berryfield
         self.bears = bears
         self.tourists = tourists     
    def __str__(self):#prints the field to the call
        x1 = False
        x2 = False
        x3 = False
        field1 = len(self.berryfield)
        bears1 = len(self.bears)
        tour1 = len(self.tourists)
        field2 = (self.berryfield)
        bears2 = (self.bears)
        tour2 = self.tourists
        berryfield = ''
        for a in range(field1):
            for x in range(field1):
                for b in range(bears1):
                    for t in range(tour1):
                          if  bears2[b].r == a and bears2[b].c == x and tour2[t].r == a and tour2[t].c == x:
                            berryfield += ("{:>4}".format("X"))
                            x1 = True       
                if x1 == False:
                    for b in range(bears1):
                        if bears2[b].r == a and bears2[b].c == x:
                            x2 = True
                            berryfield += ("{:>4}".format("B"))                                                                                                                                                                                          
                    for t in range(tour1):
                        if self.tourists[t].r == a and tour2[t].c == x:
                            x3 = True
                            berryfield += ("{:>4}".format("T"))
                if x1 == False and x2 == False and x3 == False:
                    berryfield += ("{:>4}".format(field2[a][x]))
                x1 = False
                x2 = False
                x3 = False
            berryfield += "\n"
        return berryfield
    def totalb(self):    #grows all the berries
         count = 0  
         field2 = self.berryfield
         field1 = len(self.berryfield)
         for i in range(field1):  
             for j in range(field1): 
                 count += field2[i][j]     
         return count     
    def growb(self):  #the amount berries spreading
        field1 = len(self.berryfield)
        field2 = self.berryfield
        for x in range(field1):    
            for y in range(field1):  
                if (field2[x][y] >= 1 and field2[x][y] < 10):     
                    field2[x][y] += 1         
    def spreadb(self): 
        field1 = len(self.berryfield)
        field2 = self.berryfield
        for x in range(field1): 
            for y in range(field1):  
                if (field2[x][y] == 10):  
                    if(x != field1-1 and x != 0 and  y != field1-1 and y != 0): 
                        if (field2[x+1][y] == 0):                
                            field2[x+1][y] = 1                 
                        if (field2[x-1][y] == 0):             
                            field2[x-1][y] = 1             
                        if (field2[x][y+1] == 0):          
                            field2[x][y+1] = 1             
                        if (field2[x][y-1] == 0):          
                            field2[x][y-1] = 1             
                        if (field2[x+1][y-1] == 0):              
                            field2[x+1][y-1] = 1                         
                        if (field2[x-1][y+1] == 0):                            
                            field2[x-1][y+1] = 1                         
                        if (field2[x+1][y+1] == 0):                             
                            field2[x+1][y+1] = 1                         
                        if (field2[x-1][y-1] == 0):                             
                            field2[x-1][y-1] = 1                                              
                    if (y == 0 and x != field1-1 and x != 0):                         
                        if (field2[x+1][y] == 0):         
                            field2[x+1][y] = 1          
                        if (field2[x-1][y] == 0):                            
                            field2[x-1][y] = 1                        
                        if (field2[x][y+1] == 0):                             
                            field2[x][y+1] = 1                         
                        if (field2[x-1][y+1] == 0):                           
                            field2[x-1][y+1] = 1                         
                        if (field2[x+1][y+1] == 0):                             
                            field2[x+1][y+1] = 1                                                                               
                    if (x == 0 and x != field1-1 and x != 0):                         
                        if (field2[x+1][y] == 0):                             
                            field2[x+1][y] = 1                        
                        if (field2[x][y+1] == 0):                            
                            field2[x][y+1] = 1                         
                        if (field2[x][y-1] == 0):                            
                            field2[x][y-1] = 1                         
                        if (field2[x+1][y-1] == 0):                             
                            field2[x+1][y-1] = 1                                          
                        if (field2[x+1][y+1] == 0):                            
                            field2[x+1][y+1] = 1                                                                         
                    if (y == field2[x]-1 and x != field2[x]-1 and x != 0):                         
                       if (field2[x+1][y] == 0):                             
                           field2[x+1][y] = 1                         
                       if (field2[x-1][y] == 0):                             
                           field2[x-1][y] = 1                         
                       if (field2[x][y-1] == 0):                             
                           field2[x][y-1] = 1                         
                       if (field2[x+1][y-1] == 0):                             
                           field2[x+1][y-1] = 1                         
                       if (field2[x-1][y-1] == 0):                             
                           field2[x-1][y-1] = 1                     
                    if (x == field1[x]-1 and y != field1[x]-1 and y != 0):                         
                       if (field2[x-1][y] == 0):                             
                           field2[x-1][y] = 1                         
                       if (field2[x][y+1] == 0): 
                            field2[x][y+1] = 1 
                       if (field2[x][y-1] == 0):                           
                           field2[x][y-1] = 1                        
                       if (field2[x-1][y+1] == 0):                   
                           field2[x-1][y+1] = 1                      
                       if (field2[x-1][y-1] == 0):                  
                           field2[x-1][y-1] = 1                     
                    if (x==0 and y==0):                 
                       if (field2[x+1][y] == 0):   
                           field2[x+1][y] = 1      
                       if (field2[x][y+1] == 0):
                           field2[x][y+1] = 1                         
                       if (field2[x+1][y+1] == 0):                     
                           field2[x+1][y+1] = 1                    
                    if (x == 0 and y == field1-1):    
                        if (field2[x+1][y] == 0):        
                            field2[x+1][y] = 1           
                        if (field2[x][y-1] == 0):        
                            field2[x][y-1] = 1           
                        if (field2[x+1][y-1] == 0):      
                            field2[x+1][y-1] = 1         
                    if (x == field1-1 and y == 0):  
                        if (field2[x-1][y] == 0):      
                            field2[x-1][y] = 1         
                        if (field2[x][y+1] == 0):      
                            field2[x][y+1] = 1        
                        if (field2[x-1][y+1] == 0):    
                            field2[x-1][y+1] = 1      
                    if (x == field2[x]-1 and y == field2[x]-1): 
                        if (field2[x-1][y] == 0):    
                            field2[x-1][y] = 1       
                        if (field2[x][y-1] == 0):    
                            field2[x][y-1] = 1        
                        if (field2[x-1][y-1] == 0):   
                            field2[x-1][y-1] = 1
    
    