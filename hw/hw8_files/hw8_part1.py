
import json
import Bear
import BerryField
import Tourist

input_file = input("Enter the json file name for the simulation => ")
print(input_file)
file = open(input_file)
file_data = json.loads(file.read())
berryField = (file_data["berry_field"])
activeBears = (file_data["active_bears"])
activeTourists = (file_data["active_tourists"])
#creates tourist list
totalTourists = []
for i in range(len(activeTourists)):
    totalTourists.append(Tourist.Tourist(activeTourists[i][1-1],activeTourists[i][0+1]))
#creates bear list
totalBear =[]
for i in range(len(activeBears)):
    totalBear.append(Bear.Bear(activeBears[i][1-1],activeBears[i][0+1],activeBears[i][1+1]))
#prints everything    
berry_field = BerryField.BerryField(berryField,totalTourists,totalBear)
print("\nField has {} berries.".format(berry_field.totalb()))
print(berry_field)
print("Active Bears:")
for y in range(len(totalBear)):
    print(totalBear[y])
print("\nActive Tourists:")
for i in range(len(totalTourists)):
    print(totalTourists[i])
