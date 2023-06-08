
class BerryField:
    def __init__(self,field,tourists,bears):
         self.field = field
         self.bears = bears
         self.tourists = tourists     #prints field
    def __str__(self):
        field = ''
        A = False
        B = False
        c = False
        lent = (len(self.field))
        for x in range(lent):
            for y in range(lent):
                for b in range(len(self.bears)):
                    for t in range(len((self.tourists))):
                          if  self.bears[b].r == x and self.bears[b].c == y and self.tourists[t].r == x and self.tourists[t].c == y:
                            field += ("{:>4}".format("X"))
                            A = True
                            
                            
                if A != True:
        
                    
                            
                    for b in range(len(self.bears)):
                        if self.bears[b].r == x and self.bears[b].c == y:
                            field += ("{:>4}".format("B"))                                                                                                                                                                                     
                            B = True
                    for t in range(len(self.tourists)):
                        if self.tourists[t].r == x and self.tourists[t].c == y:
                            field += ("{:>4}".format("T"))
                            c = True
                        
                if A == False and B == False and c == False:
                    field += ("{:>4}".format(self.field[x][y]))
                A = False
                B = False
                c = False
            field += "\n"
        return field
    def totalb(self):      
         total = 0         
         for x in range(len(self.field)):  
             for y in range(len(self.field)): 
                 total += self.field[x][y]     
         return total     #gros all the berries 
    def growb(self):  
        for x in range(len(self.field)):    
            for y in range(len(self.field)):  
                if (self.field[x][y] >= 1 and self.field[x][y] < 10):     
                    self.field[x][y] += 1          #determines berries spreading
    def spreadb(self): 
        for x in range(len(self.field)): 
            for y in range(len(self.field)):  
                if (self.field[x][y] == 10):  
                    if (y == len(self.field[x])-1 and x != len(self.field[x])-1 and x != 0):                         
                       if (self.field[x+1][y] == 0):                             
                           self.field[x+1][y] = 1                         
                       if (self.field[x-1][y] == 0):                             
                           self.field[x-1][y] = 1                         
                       if (self.field[x][y-1] == 0):                             
                           self.field[x][y-1] = 1                         
                       if (self.field[x+1][y-1] == 0):                             
                           self.field[x+1][y-1] = 1                         
                       if (self.field[x-1][y-1] == 0):  
                           self.field[x-1][y-1] = 1                     

                           
                    if(x != len(self.field[x])-1 and x != 0 and  y != len(self.field[x])-1 and y != 0): 
                        if (self.field[x][y-1] == 0):          
                            self.field[x][y-1] = 1             
                        if (self.field[x+1][y-1] == 0):              
                            self.field[x+1][y-1] = 1                         
                        if (self.field[x-1][y+1] == 0):                            
                            self.field[x-1][y+1] = 1 
                        if (self.field[x+1][y] == 0):                
                            self.field[x+1][y] = 1                 
                        if (self.field[x-1][y] == 0):             
                            self.field[x-1][y] = 1             
                        if (self.field[x][y+1] == 0):          
                            self.field[x][y+1] = 1  
                        if (self.field[x+1][y+1] == 0):                             
                            self.field[x+1][y+1] = 1                         
                        if (self.field[x-1][y-1] == 0):                             
                            self.field[x-1][y-1] = 1                                              
                    if (y == 0 and x != len(self.field[x])-1 and x != 0):                         
                                                     
                        if (self.field[x-1][y+1] == 0):                           
                            self.field[x-1][y+1] = 1                         
                        if (self.field[x+1][y+1] == 0):                             
                            self.field[x+1][y+1] = 1 
                        if (self.field[x+1][y] == 0):         
                            self.field[x+1][y] = 1          
                        if (self.field[x-1][y] == 0):                            
                            self.field[x-1][y] = 1                        
                        if (self.field[x][y+1] == 0):
                            self.field[x][y+1] = 1                         

                                                       
                                                                       
                                     
                    if (x == len(self.field[x])-1 and y != len(self.field[x])-1 and y != 0):                         
                       if (self.field[x-1][y] == 0):                             
                           self.field[x-1][y] = 1                         
                       if (self.field[x][y+1] == 0): 
                            self.field[x][y+1] = 1 
                       if (self.field[x][y-1] == 0):                           
                           self.field[x][y-1] = 1                        
                       if (self.field[x-1][y+1] == 0):                   
                           self.field[x-1][y+1] = 1                      
                       if (self.field[x-1][y-1] == 0):                  
                           self.field[x-1][y-1] = 1                     
                    if (x==0 and y==0):                 
                       if (self.field[x+1][y] == 0):   
                           self.field[x+1][y] = 1      
                       if (self.field[x][y+1] == 0):
                           self.field[x][y+1] = 1                         
                       if (self.field[x+1][y+1] == 0):                     
                           self.field[x+1][y+1] = 1   
                    if (x == 0 and x != len(self.field[x])-1 and x != 0):                         
                        if (self.field[x+1][y] == 0):                             
                            self.field[x+1][y] = 1                        
                        if (self.field[x][y+1] == 0):                            
                            self.field[x][y+1] = 1                         
                        if (self.field[x][y-1] == 0):                            
                            self.field[x][y-1] = 1                         
                        if (self.field[x+1][y-1] == 0):                             
                            self.field[x+1][y-1] = 1                                          
                        if (self.field[x+1][y+1] == 0):                            
                            self.field[x+1][y+1] = 1                      
                    if (x == 0 and y == len(self.field[x])-1):    
                        if (self.field[x+1][y] == 0):        
                            self.field[x+1][y] = 1           
                        if (self.field[x][y-1] == 0):        
                            self.field[x][y-1] = 1           
                        if (self.field[x+1][y-1] == 0):      
                            self.field[x+1][y-1] = 1         
                    if (x == len(self.field[x])-1 and y == 0):  
                        if (self.field[x-1][y] == 0):      
                            self.field[x-1][y] = 1         
                        if (self.field[x][y+1] == 0):      
                            self.field[x][y+1] = 1        
                        if (self.field[x-1][y+1] == 0):    
                            self.field[x-1][y+1] = 1      
                    if (x == len(self.field[x])-1 and y == len(self.field[x])-1): 
                        if (self.field[x-1][y] == 0):    
                            self.field[x-1][y] = 1       
                        if (self.field[x][y-1] == 0):    
                            self.field[x][y-1] = 1        
                        if (self.field[x-1][y-1] == 0):   
                            self.field[x-1][y-1] = 1
    
    