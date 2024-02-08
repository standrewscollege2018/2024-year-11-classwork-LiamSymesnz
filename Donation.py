#Programme determines whether the user can donate blood based of of age and weight
# Getting the age and weight of donor
keep_asking = True
while keep_asking:
    #Catches errors if your input isnt a number
    try:
        weight = float(input("How much do you weigh in kg?"))
        age = float(input("How old are you?"))
        #Prints whether your elligible or not based on your previous answers
        if (age) >= 16 and (weight) >= 50:
            print ("You are elligible to donate")
            keep_asking = False
        else:
            print ("You arent elligible to donate")
            keep_asking = False
    except ValueError:
        print ("Hey thats not a number")
