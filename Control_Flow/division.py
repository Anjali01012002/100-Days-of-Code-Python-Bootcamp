print("Please enter two numbers to divide.")
dividend = int(input('Please enter the first number to divide: '))
divisor = int(input('Please enter the second number to divide: '))

if divisor != 0:
	print(dividend, '/', divisor, "=", dividend / divisor)

print("---------------Alternative Division---------------")
if divisor != 0:
	quotient = dividend/divisor
	print(dividend, '/', divisor, "=", quotient)
	print("Program finished")


print("Another examples for control statements.")
x = 8
if x < 10:
	y=x

print('y = ', y)

print("For single statement")
x = 8
if x < 10: y=x

print('y = ', y)

print("Create the empty decisional making statement")
x = 50
if x < 10:
	pass

y = x
print('y = ', y)