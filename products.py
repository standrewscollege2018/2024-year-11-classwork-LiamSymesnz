#Programme gives product of 2 integers
keep_asking = True
second_one = True
while keep_asking:
    try:
        # Getting the first integer
        num1 = int(input("Enter a number: "))
        keep_asking = False
        #Catches errors if your input isnt a number
    except ValueError:
        print ("Hey thats not a number")

#Prints whether your elligible or not based on your previous answers
while second_one:
    try:
        # Getting the second integer
        num2 = int(input("Enter a number: "))
        second_one = False
        #Catches errors if your input isnt a number
    except ValueError:
        print ("Hey thats not a number")
        print("Please enter a number")

print(num1*num2)





num2 = float(input("Enter another number: "))
