'''This program is a quiz with at least 6 questions that will display how many questions are in the quiz, you then guess how many
you will get correct, then the questions will be asked and you will be told if you answers correctly or incorrectly. At the end the
program will display your score along with your original estimate.'''
#List of questions to be asked along with the answer and what question number, Layout is ["Question number", "Question",(Answer)]
questions =[
#The answer could be the actual name of the capital or the capital letter in the countries name
    ["Whats the capital of Spain? ", "madrid", "s"],
    ["Whats the capital of Japan? ", "tokyo", "j"],
    ["Whats the capital of New Zealand? ", "wellington", "nz"],
    ["Whats the capital of China? ", "beijing", "c"],
]

score = 0
#Asks for users name and error checks to make sure it is a valid name
    ["Whats the capital of Australia? ", "canberra", "a"],
    ["Whats the capital of Honduras? ", "tegucigalpa", "h"]
get_name = True
while get_name:
    name = input("Welcome to the quiz. What is your name? (No spaces or numbers please) \n")
    if name.strip(" ") == (""):
        print("Enter your name please ")
    elif not name.isalpha():
        print("Please enter a valid name \n")
    else:
        get_name = False

#Prints the number of questions in the quiz

print(f"\nHi {name}, there will be 6 questions about general knowledge in this quiz \n")
#Gets users estimate for how many questions they expect to get right and error checks
get_estimate = True
while get_estimate:
    try:
        estimate = int(input("How many questions do you think you will get correct? Please enter a number. \n"))
        if estimate <= -1 or estimate >= 7:
            print("Please enter a valid integer\n")
        else:
            get_estimate = False
    except ValueError:
        print("Enter a valid integer")
#Asks the user the questions and displays if answer is correct or not afters stripping all spaces to make sure answer is correct
print("")
for i in range(len(questions)):
    answer = input(questions[i][0]).strip()
    if answer.lower() == (questions[i][1]) or answer.lower() == (questions[i][2]):
        print("That is correct, Good Job! \n")
        score = score+1
    elif answer.strip(" ") == (""):
        print("You need to have an input \n")
    #If answer is wrong then it prints the correct answer
    else:
        print(f"That is incorrect. The correct answer is {questions[i][1]} or {questions[i][2]}\n")
#Prints final score in comparison to original estimate
print(f"Your final score was... {score}")
if score > estimate:
    print(f"This is higher than your original goal of {estimate}")
if score < estimate:
    print(f"That is less than your original goal of {estimate}")
if score == estimate:
    print(f"That is equal to your original goal of {estimate}")
