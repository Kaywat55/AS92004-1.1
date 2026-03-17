#constants
activities_list_tuple = [(0,"Cultural immersion",5,"Easy",800),(1,"Kayaking & Pancakes",3,"Moderate",400),(1,"Mountain Biking",4,"Difficult",900)]
shuttle_bus_cost = 80
camper_max_age = 17
camper_min_age = 5
camp_leader_age = 15

#Lists the activitys to the user
print("Number   Activity               Days    Difficulty     Cost")
print(f"{activities_list_tuple[0][0]}        {activities_list_tuple[0][1]}     {activities_list_tuple[0][2]}       {activities_list_tuple[0][3]}           {activities_list_tuple[0][4]}")
print(f"{activities_list_tuple[1][0]}        {activities_list_tuple[1][1]}    {activities_list_tuple[1][2]}       {activities_list_tuple[1][3]}       {activities_list_tuple[1][4]}")
print(f"{activities_list_tuple[2][0]}        {activities_list_tuple[2][1]}        {activities_list_tuple[2][2]}       {activities_list_tuple[2][3]}      {activities_list_tuple[2][4]}  ")

#Asking user for their name
name = ""
while len(name) == 0 or name.isdigit() == True :
    name = input("What is your name: ")
    if name == "" : print("You must enter your name!")
    if name.isdigit() == True : print("You must not enter numbers!")    

#Asking user for their age 
age = ""
while len(age) == 0 or age.isdigit() == False:
    age = (input("What is your age: "))
    if len(age) == 0 or age.isdigit() == False : print("You must enter your age!")

#seeing if user meets the age requrements 
if int(age) < camper_min_age or int(age) > camper_max_age: 
    print("Sorry, but you dont meet the age requrments to join")
    exit()

#seeing if the user can be a camp leader
if int(age) >= camp_leader_age:
    print("Beacause your over 15 you can be a camp leader")

#activity selection
activity_selection = ""
while len(activity_selection) == 0 or activity_selection.isdigit() == False:
    activity_selection = input("What number camp do you want to go on: "))
    if




