def encryptor(text, lang, key):
	temp = ''
	if lang == '1':
		for x in text:
			if x in [' ', ',', '.', '!', '-', '_', '+', '=', '%', '#', '$']:
				temp += ' '
				continue
			code = ord(x)
			if x.isupper() and code + key > 1071:
			    sym = 1039 + (code + key - 1071)
			    temp += chr(sym)
			if x.islower() and code + key > 1103:
				sym = 1071 + (code + key - 1103)
				temp += chr(sym)
			else:
				temp += chr(code + key)
		return temp
	elif lang == '2':
		for x in text:
			if not x.isalpha():
				temp += ' '
				continue
			code = ord(x)
			if x.isupper() and code + key > 90:
			    sym = 64 + (code + key - 90)
			    temp += chr(sym)
			if x.islower() and code + key > 122:
				sym = 96 + (code + key - 122)
				temp += chr(sym)
			else:
				temp += chr(code + key)
		return temp

print('Ceaser cifr')     #rus A - 1040 Я -1071  a - 1072 я - 1103
                         #eng A - 65 Z - 90  a - 97 z - 122
operation = input('1 - Encrypting\n2 - Decrypring(is not available now)\n')
lang = input('1 - Russian\n2 - English\n')
key = int(input('Key: '))
text = input('Enter text:')
if operation == '1':
	print(encryptor(text, lang, key))
else:
	print('not available')