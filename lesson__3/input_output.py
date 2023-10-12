## Вивід на консоль
print('Hello')

# Введення з консолі
## input повертає все введене
name = input('What is your name?')
lastname = input('What is your lastname')
print(type(name))
print(type(lastname))
print('Hello', name, lastname)
print('Hello', name, lastname, sep=',')
print('Hello', name, lastname, sep='\n', end='!\n')
print('Hello', name, lastname, sep='-', end='!\n')

if name == 'Andrii':
    print('Long time no see')

# Приведення типів
## Cast

a = float(input('Enter a: '))
b = int(input('Enter b: '))

print (a - b)