'''This programme takes a number and doubles it'''


keep_asking = True
while keep_asking:
    try:
        number = float(input())
        keep_asking = False
    except ValueError:
        print("Hey dumbass, thats not a number")

print(number * 2)



