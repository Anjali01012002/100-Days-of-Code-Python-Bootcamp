marks = int(input("Enter your marks: "))

if marks >= 90:
	print("Grade: A")
elif marks >= 70:
	if marks >= 85:
		print("Grade: B+")
	else:
		print("Grade: B")
elif marks >= 50:
	if marks >= 60:
		print("Grade: C+")
	else:
		print("Grade: C")
else:
	print("Grade: F(Fail)")