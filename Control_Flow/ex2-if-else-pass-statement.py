#Using pass statement:
x = int(input("Enter the value of x: "))

if x<0:
	pass #Do nothing(this will not work)
else:
	print(x)


if x>=0:
	print(x)


if x==2:
	print(x)
else:
	pass

print("Ex1- Checking the Differences- floating point equality")
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print(d1)
print(d2)
if d1 == d2:
	print("Same")
else:
	print("Different")


print("Ex2- alternative but effective- floating point equality")
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print(d1)
print(d2)
diff = d1 - d2
if diff < 0:
	diff = -diff
if diff < 0.000001:
	print('Same')
else:
	print('Different')