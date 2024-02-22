names = []
keep_asking = True
while keep_asking:
    temp_list = []
    name = input("Enter a name ")
    name.strip(" ")
    if name.lower() == "stop":
        keep_asking = False
    elif name.strip(" ") == "":
        print("Please enter a valid input ")
    else:
        get_age = True
        while get_age:
            try:
                age = int(input("Enter the age "))
                if age <= 0:
                    print("Enter a valid age")
                else:
                    get_age = False
            except ValueError:
                print("Please enter a valid input ")

        temp_list.append(name)
        temp_list.append(age)
        names.append(temp_list)
for i in range(len(names)):
    print(f"{i+1}. {names[i][0]} {names[i][1]}")
