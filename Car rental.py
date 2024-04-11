# Format of list is [Car type, number of seats, Availability]
import time
summary = []
cars_available = [
    ["Suzuki Van           |", "Number of seats - 2   |", "Available"],
    ["Toyota Corolla       |", "Number of seats - 4   |", "Available"],
    ["Honda CRV            |", "Number of seats - 4   |", "Available"],
    ["Suzuki Swift         |", "Number of seats - 4   |", "Available"],
    ["Mitsubishi Airtreck  |", "Number of seats - 4   |", "Available"],
    ["Nissan DC Ute        |", "Number of seats - 4   |", "Available"],
    ["Toyota Previa        |", "Number of seats - 7   |", "Available"],
    ["Toyota HI Ace        |", "Number of seats - 12  |", "Available"],
    ["Toyota HI Ace        |", "Number of seats - 12  |", "Available"],
]
print("Welcome to the University vehicle renting system")
time.sleep(.8)
print("The vehicles are:")
time.sleep(.8)
# Display all vehicles in a numbered list
for i in range(len(cars_available)):
    print(f"{i+1}. {cars_available[i][0]}  {cars_available[i][1]}  {cars_available[i][2]}")
time.sleep(.8)
still_ordering = True
while still_ordering:
    try:
        if cars_available[0][2] and cars_available[1][2] and cars_available[2][2] and cars_available[3][2] and cars_available[4][2] and cars_available[5][2] and cars_available[6][2] and cars_available[7][2] and cars_available[8][2] == "Not Available":

            print("Sorry we are out of cars for today, feel free to come back tomorrow ")
            still_ordering = False
            break
        chosen = int(input("Which car would you like? "))
        if chosen >= 10 or chosen <= 0:
            print("Enter a number that refers to a car ")
        else:

            if cars_available[chosen - 1][2] == ("Available"):
                print("Good choice, you have rented this car for 1 day ")
                cars_available[chosen - 1][2] = "Not Available"
                name = input("What is your name? ")
                cars_available.append(name[chosen-1])
                print("Thanks for renting a car today " + {cars_available[chosen][4]})
                for i in range(len(cars_available)):
                    print(f"{i+1}. {cars_available[i][0]}  {cars_available[i][1]}  {cars_available[i][2]}")
                time.sleep(.8)
            else:
                print("That car isnt available, please chose a different one ")
    except ValueError:
        print("Enter an integer")

