# Nested for loop

# A nested loop to display a product matrices
# Get the number of rows and columns in the table

size = int(input("Please enter the table size: "))

for row in range(1, size+1):
	for col in range(1, size+1):
		print("Row#", row, "Col#", col, sep='', end=' ')
	print()

# Converting the above program to matrix product form

size = int(input("Please enter the table size: "))

for row in range(1, size+1):
	for column in range(1, size+1):
		product = row*column
		print(product, end=' ')
	print()

# Let's talk about the permutation of the letters in word. The first letter varies from A to C

for first in 'ABC':
	for second in 'ABC':
		if second != first:
			for third in 'ABC':
				if third != first and third != second:
					print(first+second+third)