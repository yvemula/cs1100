# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:46:23 2022

@author: Yathin Vemula
"""
import hw4_util
 
run = 0
#function to find the daily per 100k people positive cases in a certain week and state
def daily(index,request,state):
    lis=[]
    list1 = hw4_util.part2_get_week(index)
    state = str(state)
    for x in hw4_util.part2_get_week(index):
        lis.append(x[0])
    list2 = lis.index(state)
    list3 = list1[list2]
    suma = list3[2]+ list3[3]+ list3[4]+ list3[5]+ list3[6]+ list3[7]+list3[8]
    return (float((suma/7)/(list3[1]/100000)))
#function to find the percent per 100k people negative cases in a certain week and state
def pct(index,request,state):
    lis=[]
    suma = 0
    state = str(state)
    list1 = hw4_util.part2_get_week(index)
    for x in list1:
        lis.append(x[0])  
    list2 = lis.index(state)
    list3 = list1[list2]
    suma = list3[2]+ list3[3]+ list3[4]+ list3[5]+ list3[6]+ list3[7]+list3[8]
    return float((suma/(suma+list3[9]+list3[10]+list3[11]+list3[12]+list3[13]+list3[14]+list3[15]))*100)
#function to find the average daily percentage of tests that are positive over the week
def quar(index,request):
    lis=[]
    a= hw4_util.part2_get_week(index)
    for x in a:
        a1=daily(index,request,x[0])
        b1 = pct(index,request,x[0])
        if (a1)>10 or b1>10:
            lis.append(x[0])
    return "Quarantine states:","\n",hw4_util.print_abbreviations(lis)
#function to find the highest daily average number of positive cases per 100k people over a given week
def high(index,request):
    lis=[]
    y = hw4_util.part2_get_week(index)
    for x in (hw4_util.part2_get_week(index)):
       
        lis.append(daily(index,request,x[0]))
    max1 = max(lis)
    max1_index= lis.index(max1)
    return max1_index,max1
    
    
#while loop to run until run becomes another number which doesnt happen
while run!=1:
    yes = True
    count = 0
    print("...")
    input_index = int(input("Please enter the index for a week: "))
    print(input_index)
    list1=hw4_util.part2_get_week(input_index)
    #if statement to check if index is inside 0-29
    if input_index<=29 and input_index>0:
        #use input of request
       input_request = str(input("Request (daily, pct, quar, high): "))
       print(input_request) 
       input_request = input_request.lower()
       #daily and pct are the only ones who use state abbreviations userly so we keep them together to ask what state
       if input_request == "daily" or input_request == "pct":
          state_name = str(input("Enter the state: "))
          print(state_name)
          #check if state is in the list of lists
          for x in list1:
              if x[0]!=state_name:
                  count+=1
        
          if count!=0:
              print("State",state_name,"not found")
          elif input_request == "daily":
              print("Average daily positives per 100K population: {:.1f}".format(daily(input_index,input_request,state_name)))
          elif input_request == "pct":
               print("Average daily positive percent: {:.1f}".format(pct(input_index,input_request,state_name)))
        #we keep the 'quar' and 'high' statements outside because they dont need user abbreviations
          #do the if State_name does not equal any of the 50 states (ex) state_name!='AZ'
          #print("State",state_name,"not found")
       if input_request == "quar":
               print("Quarantine states:")
               quar(input_index,input_request)
             ## print("Quarantine states:")
              ##print(hw4_util.print_abbreviations(quar(input_index,input_request)))
       elif input_request == "high":
               lis=[]
               for x in hw4_util.part2_get_week(input_index):
                   #calling daily functions and adding it to the list lis
                   lis.append(daily(input_index,input_request,x[0]))
              #take the max value in the list
               max1 = max(lis)
               max1_index= lis.index(max1)
               liss = list1[max1_index]
               list123 = liss[0]
               print("State with highest infection rate is",list123)
               print("Rate is","{:.1f}".format(max1),"per 100,000 people")
    #if the index is bigger than 29(weeks), then print no data for that week
    if input_index>29:
        print("No data for that week")
        #if negative index, we break the loop
    if input_index < 0:
        break
    


   
        