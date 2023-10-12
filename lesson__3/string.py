print(type(''))
print(type(""))

print('', end='!')
print("", end='!')

greeting = 'Hello'
uppercase = 'HELLO'
lowercase = 'hello'
case = 'HeLLo'

# Операції над рядками
print(3 * '-')
print(greeting.lower())
print(uppercase.lower())
print(lowercase.lower())
print(case.lower())

print(greeting.upper())
print(uppercase.upper())
print(lowercase.upper())
print(case.upper())

print(greeting.title())
print(uppercase.title())
print(lowercase.title())
print(case.title())

print(greeting.capitalize())
print(uppercase.capitalize())
print(lowercase.casefold())
print(case.casefold())

# Перевірки
print('Is digit')
print('12345'.isdigit())
print('12345a'.isdigit())
print('12345a'.isalnum())
print('12345a'.isalpha())
print(' '.isspace())
print('Count')
print(' cvc dsfs'.count(' ') > 0)
print('cvc dsfs'.index(' '))

string = 'asfaf fsfsd sdgsgs'

print('Split')
_list = string.split(' ')
print(_list)
print('Join')

print(', '.join(_list))

print('Replace')
print(string.replace('a', 'y'))

print('Strip')

print('sdfgsfgh'.strip('h'))

### Format String
print('Format String')
output = 'asdfasd ' + str(45) + ' adafsd'
print(output)

age = 34
text = 'My age is {1} {0}'.format(age, output)
text2 = 'My age is {age} {output.capitalize()}'
text3 = r"c:\Windows\Users\Andrii"
text4 = r"hello\world"
text5 = 'hello\nworld'

multiline = """
dvdfvdsfvdvdvdvf,
dssdfsvdsfvsdfvdsv,
dsfsdfvs"""

print(multiline)


print(text)
print(text2)
print(text3)
print(text4)
print(text5)

