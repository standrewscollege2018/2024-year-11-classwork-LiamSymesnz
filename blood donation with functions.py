#program out whether someone is eligible to donate blood based of weight and age
'''this program demonstrates how a function works
checks to see if the user is able to donate blood based of age and weight'''

def check(age, weight):
    if weight >= 50:
        return False
    elif age >= 16:
        return False
    else:
        return True



age = float(input("What is your age? "))
weight = float(input("What is your weight? "))
check(age, weight)

if check = True:
    print("You are elligible")
else:
    print("You arent elligible")












