# Методи які нічого не приймають і не реалізовані
def method_name():
    ...


def method_name_1():
    pass


def method_name_2():
    return NotImplemented

# Методи які нічого не повертають

def print_greetings():
    print('Hello World')

# Методи які повертають значення

def return_text():
    return 'Hello World!'

def method_tuple_of_three():
    return 1, 2, 3

if __name__ == '__main__':
    method_name()

    method_name_1()
    print(method_name_2())

    method_name_2()
    print(method_name_1())

    print_greetings()

    return_text()
    print(return_text())

    print(method_tuple_of_three())

### Функції які приймають аргументи

def function_with_one_argument(a):
    print('This is the argument: {}'.format(a))

## Передача аргумента функціїї за значення

function_with_one_argument(5)
#function_with_one_argument(input('Input your argument'))




## Передача змінної як аргум

#a = 10
#function_with_one_argument(a)
arg = input('Input your argument')
function_with_one_argument(arg)
#arg = int(arg)
arg = arg / 100

print(arg)

print(function_with_one_argument('*'))

def func_with_kwargs(**kwargs):
    print(kwargs)
    for item in kwargs:
        print(item)
        print(kwargs.get(item))


def func_with_type_checking(arg1: str, arg2: int = 50) -> None:
    print(arg1 * arg2)