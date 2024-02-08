'''This programme takes a number and doubles it'''
try:
    number = float(input())
    print(number * 2)
except ValueError:
    print("Hey dumbass, thats not a number")

