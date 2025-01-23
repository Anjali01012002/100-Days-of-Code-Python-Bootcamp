print("----------Basic Arithmetic Operator----------")

x=9
y=2

print("Addition, x + y = ",x+y)

print("Subtraction, x - y = ",x-y)

print("Multiplication, x * y = ",x*y)

print("Simple Division, x / y = ",x/y)

print("Modulus Division , x % y = ",x%y)

print("Floor Division, x // y = ",x//y)

print("Exponent, x ** y = ",x**y)
print("--------------------------------------------")

print("----------Comparison Operator----------")

a=10
b=5

print("Equal check,a(10) == b(5) ", a==b)

print("Not Equal check,a(10) != b(5) ", a!=b)

print("Less than check,a(10) < b(5) ", a<b)

print("Greater than check,a(10) > b(5) ", a>b)

print("Less than or Equal to check,a(10) <= b(5) ", a<=b)

print("Greater than or Equal to check,a(10) >= b(5) ", a>=b)
print("--------------------------------------------")

print("----------Assignment Operator----------")

x=6;y=2

x+=y  #x=x+y
print("Value of a post x+=y is ",x)

x=6;y=2

x-=y  #x=x-y
print("Value of a post x-=y is ",x)

x=6;y=2

x*=y  #x=x*y
print("Value of a post x*=y is ",x)

x=6;y=2

x/=y  #x=x/y
print("Value of a post x/=y is ",x)

x=6;y=2

x%=y  #x=x%y
print("Value of a post x%=y is ",x)

x=6;y=2

x//=y  #x=x//y
print("Value of a post x//=y is ",x)

x=6;y=2

x**=y  #x=x**y
print("Value of a post x**=y is ",x)
print("--------------------------------------------")

print("----------Logical Operators----------")

x=True
y=False

print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)
print('not y is', not y)

a=1
b=0

print('a and b is', a and b)

print('a or b is', a or b)

print('not a is', not a)
print('not b is', not b)
print("--------------------------------------------")

print("----------Membership Operators----------")
var1="Hello World"
var2={1:'a',2:'b','all':4}

print('H' in var1)

print('hello' in var1)

print('hello' not in var1)

print(1 in var2)

print(2 in var2)

print('a' in var2)

print('all' in var2)
print("--------------------------------------------")

print("----------Identity Operators----------")

var1=5; print(var1)
print(id(var1))

var2=5; print(var2)
print(id(var2))

var3='Hello'; print(var3)
print(id(var3))

var4='Hello'; print(var4)
print(id(var4))

var5=[1,2,3]; print(var5)
print(id(var5))

var6=[1,2,3]; print(var6)
print(id(var6))

print(var1 is var2)

print(var3 is var4)

print(var5 is var6)

print(var5 is not var6)
print("--------------------------------------------")