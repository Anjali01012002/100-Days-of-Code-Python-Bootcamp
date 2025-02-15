# Definite Vs Indefinite loops
# Example for definite loop

n = 1
while n <= 10:
	print(n)
	n += 1

#  Example-2 for definite loop

n = 1
stop = int(input("Enter the number: "))
while n <= stop:
	print(n)
	n += 1

# Example-3 for Indefinite loop

done = False
while not done:
	entry = int(input("Enter the number: "))
	if entry == 999:
		done = True
	else:
		print(entry)