'''This programme takes a number and doubles it'''

# Start a loop for error catching
keep_asking = True
while keep_asking:
    # Takes input then doubles it if it is a number
    try:
        number = float(input("Enter a positive number"))
        if number  >= 0:
            keep_asking = False
        else:
            print("Hey dumbass, thats not a positive number!")
    except ValueError:
        print(f"Hey dumbass, thats not a number")

# Print the result
print (f"{number} doubled is {number * 2}")



