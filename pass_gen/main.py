from random import *

digist = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'
chars = ''

def generate_password(l, ch):
	temp = ''
	for i in range(l):
		temp += choice(ch)
	return temp

passwords_count = int(input('Enter count of passwords you want to be generated: '))
pass_len = int(input('Length of one password: '))
add_num = input('Add numbers(y - yes | n - no) - ')
add_upper = input('Add uppercase letters(y - yes | n - no) - ')
add_lower = input('Add lowerrcase letters(y - yes | n - no) - ')
add_symbol = input('Add symbols(y - yes | n - no) - ')
del_ambiguous = input('Delete ambiguous symbols(y - yes | n - no) - ')

if add_num == 'y':
	chars += digist
if add_upper == 'y':
	chars += uppercase_letters
if add_lower == 'y':
	chars += lowercase_letters
if add_symbol == 'y':
	chars += punctuation
if del_ambiguous == 'y':
	for i in chars:
		if i in ambiguous:
			chars = chars.replace(i, '')

for x in range(passwords_count):
	print(f'{x + 1} password: {generate_password(pass_len, chars)}')