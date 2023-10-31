
def func(param):
    return param * 2

var_func = func

## Lambda

var_lambda = lambda x: x * 2
var_lambda2 = lambda x: x ** 3

var_lamb = lambda x, y: x * y
var_max = lambda x, y: x if x > y else y
var_empty = lambda: print('Hello World')
var_empty2 = lambda: var_max (var_lambda(2), var_lambda2(2))

if __name__ == '__main__':
    print(func(2))
    print(func('2'))
    print(var_func('2'))
    print('lambda')
    print(var_lambda)
    print(var_lambda(2))
    print(var_lambda('2'))
    print(var_lambda2)
    print(var_lambda2(3))
    print('Lamb with 2 parametrs')
    print(var_lamb (2, 3))
    print((lambda x, y,: x * y)(3, 4))
    print(var_max(5, 6))
    print(var_max(6,8))

    var_empty()
    print(var_empty2(2))

    for i in range(0, 11):
        print((lambda x: x * 2)(i))