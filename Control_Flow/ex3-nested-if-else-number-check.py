# To Check the number between 0 and 10
value = int(input("Please enter an Integer value in the range o....10:"))
if value >= 0:
	if value <= 10:
		print('In Range')

print("Done")

#To check the number between 0 and 10 only with single if statement
x = int(input("Please enter an Integer value in the range o....10:"))
if x >= 0 and x <= 10:
		print('In Range')
print("Done")

# Must and should use else part
y = int(input("Please enter an Integer value in the range o....10:"))
if y >= 0:
	if y <= 10:
		print(y,"In Range")
	else:
		print(y, "is too large")
else:
	print(y, "is too small")

print("Done")