# Get the input and split into two variables

# Check which is higher and then either count up or down from the first to the second
# If they are equal, print 'Same!'

num1, num2 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
if num1 >= num2:
  for i in range(num1, num2 +1):
    print(i)
elif num1 == num2:
  print ("Same!")
else:
  for i in range(num2, num1 -1):
    print(i)
