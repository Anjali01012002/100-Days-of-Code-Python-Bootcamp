# Logic Complexity

# Finding the maximum value: 

print("Please enter four integer values.")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
	max = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
	max = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
	max = num3
else:
	max = num4

print("The maximum number entered was: ",max)

# Logic complexity can be made simple

print("Please enter four integer values.")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

max = num1
if num2 > max:
	max = num2
if num3 > max:
	max = num3
if num4 > max:
	max = num4

print("The maximum number entered was: ",max)