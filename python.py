def inputs():
    print("Enter all the states of the USA you can think of")
    state_name = "  "
    while state_name != "":
        state_name = input("Enter a state name (press enter whyen you can't thik of any):")
        state_list.append(state_name)

def states():
    print("These are all the states you could think of")
    state_count = 0
    while state_count < len(state_list):
        print(state_list[state_count])
        state_count += 1

state_list = []
inputs()
states()



        