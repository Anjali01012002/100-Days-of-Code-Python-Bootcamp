print("----------More on Arithmetic operator----------")

num1 = 4
num2 = 8

total = num1 + num2
print(num1, "+" ,num2, "=", total)

print("----------'+' and '-' Unary Operators----------")
x,y,z=3,-4,0
x = -x
y = -y
z = -z
print(x, y, z)

print("----------Arithmetic Operators limitations of the data types----------")
value1=2.0 ** 10
print(value1)

value2=2.0 ** 100
print(value2)

value3=2.0 ** 1000
print(value3)

# value4=2.0**10000
# print(value4)

#truncation
print(25 // 4, 4 // 25)
# / operator applied to two integers produces a floating-point number
print(25 / 4, 4 / 25)
# %-remainder with modulus operator
print(25 % 4, 4 % 25)

#more lines by using the backslash(/) symbol at the end of an incomplete line
ten=10.0
ten_by_three = 10.0 / 3.0
zero=ten - ten_by_three - ten_by_three - ten_by_three\
- ten_by_three - ten_by_three - ten_by_three \
-ten_by_three - ten_by_three - ten_by_three \
-ten_by_three
print(zero)

# python statement spread over two lines in the source code
x=(int(input("Please enter an integer"))
	+(y-2) +16) *2

print(x)

y=10
x=(int(input("Please enter an integer"))
	+(y-2) +16

	) *2

print(x)

#mixed type expression
x = 4
y = 2.5
addition = x + y
print(addition)

print("----------Operator Precedence and associativity----------")
print(2 + 3 * 4 / 2)

print((2+3)*4)

print(2-3-4)

print("----------Chained Assignment----------")
w=x=y=z=0
print(w, x, y, z)

#formatting expressions
#3x+2y-5
3*x + 2*y - 5
3 * x + 2 * y - 5