# if conditions:
#   expression

a = 4
b = 5
var_string_decimal = '34'
var_string = 'Hi'
none = 'True'

if a > b:
    print("a > b")
else:
    print("a < b")

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("no one condition is true")

## Nested if (Вкладені if)

if a > b:
    if a > 5:
        print('nested if: a > b and a > 6')
    else:
        print('nested if: a > b and a<= 6')

if isinstance(a, int):
    print('a is int')
elif none is None:
    print('none is None')
elif isinstance(var_string, str):
    print(var_string, type(var_string))

if var_string_decimal.isdigit():
    print(var_string_decimal)
    print(type(var_string_decimal))
    new_int = int(var_string_decimal)
    print(new_int)
    print(type(new_int))

## Оператори для перевірки умов

if a > b:
    print('a')
if a >= b:
    print(a)
if a < b:
    print(b)
if a <= b:
    print(b)
if a == b:
    print(a)
if a != b:
    print(a)
if none is None:
    print(none)
if var_string is str:
    print(var_string)

if not none:
    print('something')
if none is not None:
    print('something')

## Декілька умов

if (a > b) and (a > 3):
    print(a)
if (a > b or a > 30) and b // 2 == 0:
    print('OR')


######## match-case

command = 'Hello'
match command:
    case 'Hi':
        print('Hi to you')
    case 'good morning':
        print('Good Morning to you too')
    case 'Hello':
        print('Hello to you')
    case 'Wazzup':
        print('Wazzup')
    case _:
        print('I don\'t understand you')

if command == 'hi':
    print('Hi to you')
elif command == 'good morning':
    print('Good Morning to you too')
elif command == 'hello':
    print('Hello to you')
elif command == 'Wazzup':
    print('Wazzup')
else:
    print('I don\'t understand you')