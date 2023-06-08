class Bear:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
        self.kill = False
        self.sleep = False
        self.turns = 0
        self.left = False
        self.eat = 0
    #prints bear 
    def __str__(self):
        string = "Bear at ({},{}) moving {}".format(str(self.r),str(self.c),self.d)
        return string
    #moves bear
    def move(self):
        #if self.asleep == False:
            if self.d == "N":
                self.r -= 1
            elif self.d == "NE":
                self.r -= 1
                self.c += 1
            elif self.d == "E":
                self.c += 1
            elif self.d == "SE":
                self.r += 1   
                self.c += 1
            elif self.d == "S":
                self.r += 1
            elif self.d == "SW":
                self.r+= 1
                self.c-= 1
            elif self.d == "W":
                self.c -= 1  
            elif self.d == "NW":
                self.r-= 1
                self.c-= 1
 
