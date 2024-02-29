import time
''' code to display avaibel rental cars and allow people to borrow until program is reset'''

#initialize lists
cars = ['Suzuki Van', 'Toyota Corolla', 'Honda CRV', 'Suzuki swift', 'Mitsubishi Airtrek', 'Nissan DC Ute', 'Toyota Previa', 'Toyota Hi Ace', 'Toyota Hi Ace']
seats = [2, 4, 4, 4, 4, 4, 7, 12, 12]
available = [0, 0, 0, 0, 0, 0, 0, 0, 0]
customer =[]
cont_ask = True

'''looping code to ask each new customer about what car they want'''
#to repeat while there are still customers
while cont_ask == True:

    print ('Welcome to the University vehicle rental system\nThe vehicles are:')
    #display every car, how many seats, and whether it is unavailable in a numbered list

    for i in range(0, 9):
        time.sleep(0.3)
        print (f"{i+1}. {cars[i]} ({seats[i]})", end="")
        if available[i] == 1:
            print(" - Unavailable")
        else:
            print()

    time.sleep(0.3)
    #set up loop to keep asking for vehicle number while invalid
    valid_car = False
    already_booked = False
    while valid_car == False:
        #check if input is int
        time.sleep(0.6)
        try:
            booked_car = int(input("Which vehicle would you like to book? "))
            #check in input is in specified range
            if booked_car<=9 and booked_car>=1:
                #break out of loop (stop asking)
                valid_car = True
                #check if car is already booked
                if available[booked_car-1] == 0:
                    available[booked_car-1] = 1
                else:
                    print ("** This vehicle is already booked. Please choose another **\n")
                    already_booked = True
            #check if
            elif booked_car == 0:
                valid_car = True
                cont_ask = False
                print()
                time.sleep(1)
            else:
                print ("Please enter a valid vehicle number.")
        except ValueError:
            print ("Please enter a valid vehicle number.")

    #only continue if car is not booked already and if booked_car is not 0
    if already_booked == False and cont_ask ==True:
        ##time to ask for the seats required yipeeee
        ##validseat
        time.sleep(0.6)
        #loop to ask for name
        valid_name = False
        while valid_name == False:
            time.sleep(0.3)
            name = input("What is your name? ")
            time.sleep(0.3)
            #check is name is empty or space character
            if name.strip() != "":
                print (f"Thanks {name}\n")
                #add customers detais to 'customer' list
                customer.append([name, booked_car-1])
                #stop asking for name
                valid_name = True
                time.sleep(1)
            else:
                print ("Please enter a valid name.")


####################### Display summary of daily bookings ################################
'''display all cars borrowed'''
print ("Daily Summary")
time.sleep(0.3)
#check if there were any customers
if len(customer) ==0:
    print("No customers today.")
else:
    #print all customer name and their car
    for i in range(0, len(customer)):
        print(f"{cars[customer[i][1]]} - {customer[i][0]}")
        time.sleep(0.3)

