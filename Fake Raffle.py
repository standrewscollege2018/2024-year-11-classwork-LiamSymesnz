import random
print("Welcome to the raffle, Please enter names of participants, enter 'done' when finished! ")
prize_worth = True
while prize_worth:
        prize = str(input("Enter something to be the prize, this could be an item, a person or a service: "))

        if not prize.isalpha():
            print('Enter only letters')
            continue
        else:
            break
money = True
while money:
    try:
        prize_money = float(input("Enter how much the prize is worth! "))
        if prize_money <= 0:
            print("Enter a positive number genius ")
        else:
            money = False
    except ValueError:
        print ("Hey Genius, thats not a number ")
person_asking = True
person = []
while person_asking:

    name = str(input("Enter someone to add to the raffle, say 'done' to end! "))
    if name.lower() == "done":
        if len(person) == (0):
            print("You need to enter some participants ")
        else:
            person_asking = False
            winner = random.randint(0, len(person) - 1)
            print(f"The person who won the raffle was {person[winner]}")
            prize_money = str(prize_money)
            print(("The value of the prize was ") + (prize_money))
    elif not name.isalpha():
        print("Enter only letters! ")

    else:
        person.append(name)




