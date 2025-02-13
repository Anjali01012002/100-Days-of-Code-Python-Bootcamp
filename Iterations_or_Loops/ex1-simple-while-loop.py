#Printing numbers from 1 to 5 using print statement
print(1)
print(2)
print(3)
print(4)
print(5)

#The same can be achieved using "while" loop

count = 1
while count <= 5:
	print(count)
	count += 1

#Let's check the program with the count = 6 instead of 5 and see what happened

count = 6
while count <= 5:
	print(count)
	count += 1

#Code to count the number of correct entries of "Y or y"
#Counts up from zero. The user continues the count by entering
#The user discontinues the count by entering 'N'.

count = 0
entry = 'Y'

while entry != 'N' and entry != 'n':
	print(count)
	entry = input('Please enter "Y" to continue or "N" to quit: ')
	if entry == 'Y' or entry == 'y':
		count += 1
	elif entry != 'N' and entry != 'n':
		print('"'+entry+'" is not a valid choice')


#Allow the user to enter a sequence of non-negative integers. the user ends the list with negative integer.
#At the end the sum of the non-negative numbers entered is displayed. The program prints zero if the user provides no non-negative numbers.
 
entry = 0
sum = 0

print("Enter numbers to sum, negative number ends list: ")

while entry >= 0:
	entry = int(input("Enter positive numbers for addition: "))
	if entry >= 0:
		sum += entry
print("Sum =", sum)

# print x only if x is non-zero
x = int(input("Enter Number: "))
while x:
	print(x)
	x -= 1
# is equivalent to
x = int(input("Enter Number: "))
while x != 0:
	print(x)
	x -= 1

# How to use floating point numbers properly in any loops
# Example below shows an incorrect way of using the floating point number

x = 0.0
while x != 1.0:
	print(x)
	x += 0.1
print("Done")

# The correct method is either using x += 0.125 or using x <= 1.0 in the while statement. using x += 0.125 in increment statement

x = 0.0
while x != 1.0:
	print(x)
	x += 0.125
print("Done")

# Using x <= 0.1 in while statement
x = 0.0
while x <= 1.0:
	print(x)
	x += 0.1
print("Done")