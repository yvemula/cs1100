import json
import BerryField
import Bear
import Tourist
 
#inputs file
input_file = input("Enter the json file name for the simulation => ")
print(input_file)
#file = "bears_and_berries_1.json"
#opens everything
fi = open(input_file)
file_data = json.loads(fi.read())
berryfield1 = (file_data["berry_field"])
activeBears1 = (file_data["active_bears"])
reserveBears1 =(file_data["reserve_bears"])
activeTourists1 = (file_data["active_tourists"])
reserveTourists1 = (file_data["reserve_tourists"])
#tourist list
tourists = []
bears =[]
rbears = []
rtourists = []
for x in range(len(activeTourists1)):
    tourists.append(Tourist.Tourist(activeTourists1[x][0],activeTourists1[x][1]))
for x in range(len(activeBears1)):
    bears.append(Bear.Bear(activeBears1[x][0],activeBears1[x][1],activeBears1[x][2]))
for x in range(len(reserveBears1)):
    rbears.append(Bear.Bear(reserveBears1[x][0],reserveBears1[x][1],reserveBears1[x][2]))
for x in range(len(reserveTourists1)):
    rtourists.append(Tourist.Tourist(reserveTourists1[x][0],reserveTourists1[x][1]))
#prints starting configuration
print("\nStarting Configuration")  
berryfield = BerryField.BerryField(berryfield1,tourists,bears)
print("Field has {} berries.".format(berryfield.totalb()))
print(berryfield)
print("Active Bears:")
for x in range(len(bears)):
    print(bears[x])
print("\nActive Tourists:")
for x in range(len(tourists)):
    print(tourists[x])
tu = 1
while True:
    #prints the turn number
    if tu == 1:
        print("\nTurn: {}".format(tu))
    else:
        print("\n\nTurn: {}".format(tu))
    #grows and spreads berries
    berryfield.growb()
    berryfield.spreadb()
    #sees if any tourists and bears occupy the same spot
    bl = len(bears)
    tl = len(tourists)
    for x in range(bl):
         for y in range(tl):
             if  bears[x].c == tourists[y].c and bears[x].r == tourists[y].r :
                 
                 bears[x].kill = True
                 tourists[y].die = True
    #counter for seeing how many tourists get removed for list to avoid errors
    count = 0
    for x in range(tl):
        if tourists[x-count].die == True or tourists[x-count].scared == True:
            print("{} - Left the Field".format(tourists[x-count]))
            #removes tourists from the list of active tourists
            tourists.remove(tourists[x-count])
            count += 1
    for b in range(bl):
        #if the bear got a kill it takes a quick nap
        if bears[b].sleep == True:
            bears[b].turns -= 1
        if bears[b].kill == True:
            bears[b].sleep = True
            bears[b].kill = False
            bears[b].turns = 4
        if bears[b].turns == 0:
            bears[b].sleep = False
        #if the bear is awake and has not bailed yet it continues
        if bears[b].sleep == False and bears[b].left == False:
            while True:
                #bear eats all the bears leave the field with 0 berries at that spot
                b123 = berryfield.field[bears[b].r][bears[b].c]
                bears[b].eat += b123
                berryfield.field[bears[b].r][bears[b].c] = 0
                #moves bear
                bears[b].move()
                #check to see if a tourist get eaten, if it does then bear stops moving
                for t in range(len((tourists))):
                    if  bears[b].c == tourists[t].c and bears[b].r == tourists[t].r :
                        bears[b].kill = True
                        tourists[t].die = True
                if bears[b].kill == True:
                    break
                bflen = len(berryfield.field)
                #if bear goes off field he stops moving
                if bears[b].r > bflen-1:
                    bears[b].left = True
                    break
                elif bears[b].r < 0:
                    bears[b].left = True   
                    break
                elif bears[b].c > bflen-1:
                    bears[b].left = True
                    break
                elif bears[b].c < 0:
                    bears[b].left = True
                    break
                bears123 = berryfield.field[bears[b].r][bears[b].c]
                bears[b].eat += bears123
                berryfield.field[bears[b].r][bears[b].c] = 0
                if bears[b].eat >= 30:#if more than 30 berries
                    bs123 = bears[b].eat - 30
                    berryfield.field[bears[b].r][bears[b].c] =  bs123
                    break
        bears[b].eat = 0
    #if the tourist is alive it looks around to see if a bears around            
    for t in range(len(tourists)):
        if tourists[t].die == False:
            if tourists[t].sees(bears) >= 3:
                tourists[t].scared = True
            if tourists[t].sees(bears) > 0:
                tourists[t].turns = 0
            if tourists[t].sees(bears) == 0:
                tourists[t].turns += 1
    
    #if bear gets a kill it goes to bed        
    for c in range(len(bears)):
        if bears[c].kill == True:
            bears[c].turns = 3
            bears[c].kill = False
            bears[c].sleep = True
    #if a tourist has not seen a bear for 3 turns they bail
    for c in range(len(tourists)):
        if tourists[c].turns == 3:
            tourists[c].bored = True
    # if the tourist sees more than 3 bears it gets scared and bails
    for t in range(len(tourists)):
        if tourists[t].sees(bears) >= 3:
            tourists[t].scared = True
    count = 0 
    for b in range(len(bears)):
        if bears[b-count].left == True:
            print("{} - Left the Field".format(bears[b-count]))
            bears.remove(bears[b-count])
            count +=1
    #counter for seeing how many tourists get removed for list to avoid errors
    count = 0
    for c in range(len(tourists)):
        if tourists[c-count].scared == True or tourists[c-count].bored == True or tourists[c-count].die == True:
            print("{} - Left the Field".format(tourists[c-count]))
            tourists.remove(tourists[c-count])
            count += 1
    #sees if a bear can enter
    lr = len(rbears)
    totalBerr = berryfield.totalb()
    if lr > 0 and totalBerr > 500:
        bears.append(rbears[0])
        rbears.remove(rbears[0])
        print(("{} - Entered the Field".format(bears[0-1])))
     #sees if a tourist can enter  
    act1 = len(bears)
    ltr = len(rtourists)
    if ltr>0 and act1 > 0:
        tourists.append(rtourists[0])
        rtourists.remove(rtourists[0])
        print(("{} - Entered the Field".format(tourists[0-1])))
    #prints update every 5 turns
    if tu % 5 == 0:
        print("Field has {} berries.".format(berryfield.totalb()))
        print(berryfield)
        print("Active Bears:")
        for bear in range(len(bears)): 
            if bears[bear].sleep == True and bears[bear].turns -1 >0:
                print("{} - Asleep for {} more turns".format(bears[bear],(bears[bear].turns-1)))
            else:
                print(bears[bear])
        print("\nActive Tourists:")
        for tourist in range(len(tourists)):
            print(tourists[tourist])       
    tu += 1
    act12 = len(bears)#end simulatuion
    ltrb = len(rbears)
    if act12 == 0 and ltrb== 0:
        break
#prints final update
print("Field has {} berries.".format(berryfield.totalb()))
print(berryfield)
print("Active Bears:")
bearlen = len(bears)
for x in range(bearlen): 
    if bears[x].turns -1 >0 and  bears[x].sleep == True :
        print("{} - Asleep for {} more turns".format(bears[x],(bears[x].turns-1)))
    else:
        print(bears[x])
print("\nActive Tourists:")
for g in range(len(tourists)):
    print(tourists[g])       
print()






