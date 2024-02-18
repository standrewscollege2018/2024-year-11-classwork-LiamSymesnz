#Add a list
list = []
keep_adding = True
while keep_adding:
    add = input("Enter a name or number to add to a list, say stop to stop ")
    # If input is "Stop" with any capitals then stop the code and print list
    if add.lower() =="stop":
        #Sort list into alphabetical or numerical order and then print list
        for i in range(len(list)):
            list = (sorted(list))
            #F strings  convert input into variables by using curly brackets, anything inside curly brackets gets turned into the vairable
            print(f"{i+1}. {list[i]}")
        keep_adding = False
    #Dont allow blank inputs
    elif add.strip(" ") == "":
        print("Please enter a valid input ")
    #Add valid input to list
    else:
        list.append(add)

