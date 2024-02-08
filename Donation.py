#Programme determines whether the user can donate blood based of of age and weight
keep_asking = True
while keep_asking:
    try:
        # Getting the age and weight of donor
        weight = float(input("How much do you weigh in kg: "))
        age = float(input("How old are you: "))
        #Catches errors if your input isnt a number
        if age >= 16 and (weight) >= 50:
            keep_asking = False
        elif (age) <=0:
            print("Please enter a positive number")
        elif weight <=0:
            print("Please enter a positive number")
        else:
            print ("You arent elligible to donate")
            keep_asking = False
    except ValueError:
        print ("Hey thats not a number")
#Prints whether your elligible or not based on your previous answers
if (age) >= 16 and (weight) >= 50:
    print ("You are elligible to donate")
