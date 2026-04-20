#constants
activities_list_tuple = [(0,"Cultural immersion",5,"Easy",800),(1,"Kayaking & Pancakes",3,"Moderate",400),(2,"Mountain Biking",4,"Difficult",900)]
shuttle_bus_cost = 80
camper_max_age = 17
camper_min_age = 5
camp_leader_age = 15
meal_options = ["standard","vegeterian","vegan"]

#Lists the activitys to the user
print("Number   Activity               Days    Difficulty     Cost")
print(f"{activities_list_tuple[0][0]}        {activities_list_tuple[0][1]}     {activities_list_tuple[0][2]}       {activities_list_tuple[0][3]}           {activities_list_tuple[0][4]}")
print(f"{activities_list_tuple[1][0]}        {activities_list_tuple[1][1]}    {activities_list_tuple[1][2]}       {activities_list_tuple[1][3]}       {activities_list_tuple[1][4]}")
print(f"{activities_list_tuple[2][0]}        {activities_list_tuple[2][1]}        {activities_list_tuple[2][2]}       {activities_list_tuple[2][3]}      {activities_list_tuple[2][4]}  ")

#Asking user for their name and checks if valid.
name = ""
while len(name) == 0 or name.isalpha() == False :
    name = input("What is your name: ").title().strip()
    if name == "" : print("You must enter your name!")
    elif name.isalpha() == False : print("You must not enter something!")    

#Asking user for their age and checks if valid.
age = ""
while len(age) == 0 or age.isdigit() == False:
    age = (input("What is your age: ")).strip()
    if len(age) == 0 or age.isdigit() == False : print("You must enter your age!")

#seeing if user meets the age requrements.
if int(age) < camper_min_age or int(age) > camper_max_age: 
    print("Sorry, but you dont meet the age requrments to join")
    exit()

#seeing if the user is over 15.
if int(age) >= camp_leader_age:
    print("Beacause your 15+ you can be a camp leader")

#asks if user wants to be a camp leader and checks if vaild.
    camp_leader_option = ""
    while camp_leader_option == "" or camp_leader_option.isdigit() == True or camp_leader_option != "yes" or camp_leader_option != "no":
        camp_leader_option = input("Do you want to be a camp leader: ").lower().strip()
        if camp_leader_option == "": print("You must not leave it blank!")
        if camp_leader_option.isdigit() == True: print("You must not enter numbers!")
        if camp_leader_option != "yes" and camp_leader_option != "no" : print("You must only enter yes or no!")
        if camp_leader_option != "" and camp_leader_option.isdigit() == False:
            if camp_leader_option == "yes":
                camp_leader_wanted = "do"
                break
            if camp_leader_option == "no":
                camp_leader_wanted = "don't"
                break
        
#asking the user what activity they would like to do.
activity_selection = ""
while activity_selection == "" or activity_selection.isdigit() == False:
    activity_selection = input("What number camp do you want to go on: ").strip()
    if activity_selection == "": print("You must enter something!")
    if activity_selection.isdigit() == False: print("You must enter a valid number!")
    if activity_selection.isdigit() == True :
          if int(activity_selection) > len(activities_list_tuple) : print("You must enter a vaild camp number!")

#Asking for type of meal and checks if vaild.
meal_input = ""
while meal_input == "" or meal_input.isdigit() == True or meal_input not in meal_options:
    meal_input = input(f"What meal do you want: standard, vegeterian, vegan: ").lower().strip()
    if meal_input == "": print("You must enter something!")
    if meal_input.isdigit() == True: print("You must not enter a number!")
    if meal_input != "" and meal_input.isdigit() == False:
        if meal_input not in meal_options: print("That is not a valid meal")

# Asking for Suttle bus option and checks if vaild.
shuttle_bus_option = ""
while shuttle_bus_option == "" or shuttle_bus_option.isdigit() == True or shuttle_bus_option != "yes" or shuttle_bus_option != "no":
    shuttle_bus_option = input("Do you want the shuttle bus (80$) ").lower().strip()
    if shuttle_bus_option == "": print("You must not leave it blank!")
    if shuttle_bus_option.isdigit() == True: print("You must not enter numbers!")
    if shuttle_bus_option != "yes" and shuttle_bus_option != "no": print("You must only enter yes or no!")
    if shuttle_bus_option != "" and shuttle_bus_option.isdigit() == False:
        if shuttle_bus_option == "yes":
            shuttle_bus_needed = "do"
            break
        if shuttle_bus_option == "no":
            shuttle_bus_needed = "don't"
            break

#Listing everything back to user.
print(f"Hello {name} you are {age}. You are going to the {activities_list_tuple[int(activity_selection)][1]} camp, \
which is {activities_list_tuple[int(activity_selection)][3]}. Your meal is {meal_input}. You {shuttle_bus_needed} need the shuttle bus.")

#Camp total cost calculation.
camp_cost = activities_list_tuple[int(activity_selection)][4]
if shuttle_bus_needed == "do":
    camp_cost += shuttle_bus_cost
if shuttle_bus_needed == "don't":
    camp_cost += camp_cost

#confirmation for camp and checks if vaild.
confirmation = ""  
while confirmation == "" or confirmation.isdigit() == True or confirmation != "yes" or confirmation != "no":
    confirmation = input(f"Plese comfirm your stay with a price of ${camp_cost} ").lower().strip()
    if confirmation == "": print("You must not leave it blank!")
    if confirmation.isdigit() == True: print("You must not enter numbers!")
    if confirmation != "yes" and confirmation != "no" : print("You must only yes or no")
    if confirmation != "" and confirmation.isdigit() == False:
        if confirmation == "yes":
            print("Enjoy your stay")
            break
        if confirmation == "no":
            print("Bye")
            break