# "for" loop # Numenric values starts from "0" in Python

for n in (1,2,3,4,5,6,7,8,9,10):
	print(n)

# 'for' loop using "range" function

for n in range(0,11):
	print(n)

# General form of "range" function:- range(begin, end, step)

for  n in range(21, 4, -3):
	print(n, end=' ')
print('\n')

# 'for' loop to sum from 1 to 100

sum = 0
for i in range(1,100):
	sum+=i
print(sum)

# We can use a for loop to iterate over the character that comprise a string

word = input('Enter a word: ')
for letter in word:
	print(letter, end=' ')
print('\n')

# 'for' loop to iterate over a literal string

for c in 'PRUTHIVIRAJA L':
	print('[', c, ']', end=' ', sep='')
print()
print()
print()
print()

# 'for' loop can be used to count the number of vowels in the text provided by the user
word=input('Enter text: ')
vowel_count = 0
for c in word:
	if c == 'A' or c == 'a' or c == 'E' or c == 'e' or c == 'I' or c == 'i' or c == 'O' or c == 'o' or c == 'U' or c == 'u' :
		print(c,', ', sep='',end='')
		vowel_count += 1
print('(', vowel_count, 'vowels)', sep='')
