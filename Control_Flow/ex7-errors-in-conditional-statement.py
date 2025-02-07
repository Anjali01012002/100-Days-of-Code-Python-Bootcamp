# Errors in conditional statements

# x > 0 or x <= 10(True always- Tautology)
# x < 0 and x > 10(False always- Contradictions)

value = int(input("Enter a number"))
if value < 0 or value > 10:
	print(value)

x = 4
if 1 <= x <= 3:
	print("ok")

if (x == 1) or 2 or 3:
	print("ok")

if (x == 1) or x == 2 or x == 3:
	print("ok")


# Digit to word converter (Syntax error)

value = int(input("Please enter an integer in the range 0...5: "))
answer = "Not in range" #Default Answer
if value == 0:
	answer = "Zero"
elif value == 1:
	answer = "one"
elif value == 2:
	answer = "two"
elif value == 3:
	amswer = "three"   # Replace m in answer by n
elif value == 4:
	answer = "four"
elif value == 5:
	answer = "five"
print("The number you entered was", answer)