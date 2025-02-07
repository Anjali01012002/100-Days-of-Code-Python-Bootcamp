# Multi-way Versus Sequential Conditionals

#Using a multi-way conditional ststement

value = int(input("Enter a number: "))
if value == 0:
	print("Zero")
elif value == 1:
	print("One")
elif value == 2:
	print("Two")
elif value == 3:
	print("Three")
elif value == 4:
	print("Four")
elif value == 5:
	print("Five")
print("Done")

#Using sequential conditional statements
value = int(input("Enter a number: "))
if value == 0:
	print("Zero")
if value == 1:
	print("One")
if value == 2:
	print("Two")
if value == 3:
	print("Three")
if value == 4:
	print("Four")
if value == 5:
	print("Five")
print("Done")

#Comparing Multi-way Versus Sequential conditionals

print("Ex1: Multi-way")
num = int(input("Enter a number: "))
if num == 1:
	print("You entered one")
elif num == 2:
	print("You entered Two")
elif num > 5:
	print("You entered a number greater than five")
elif num == 7:
	print("You entered seven")
else:
	print("You entered some other number.")


print("Ex1: Sequential-way")
num = int(input("Enter a number: "))
if num == 1:
	print("You entered one")
if num == 2:
	print("You entered Two")
if num > 5:
	print("You entered a number greater than five")
if num == 7:
	print("You entered seven")
else:
	print("You entered some other number.")