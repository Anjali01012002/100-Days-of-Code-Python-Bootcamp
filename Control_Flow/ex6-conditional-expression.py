# Without conditional expression

dividend = int(input('Enter Dividend: '))
divisor = int(input('Enter Divisor: '))

if divisor != 0:
	print(dividend/divisor)
else:
	print('Error, cannot divide by zero')

# With conditional expression

dividend = int(input('Enter Dividend: '))
divisor = int(input('Enter Divisor: '))

message = dividend/divisor if divisor != 0 else 'Error, cannot divide by zero'
print("Message: ",message)

#Finding absolute Value
n = int(input("Enter a number: "))
print('/',n,'/ = ',(-n if n < 0 else n), sep="")
print("Without sep")
print('/',n,'/ = ',(-n if n < 0 else n))
print(abs(n))