var_set = set()

print(var_set)
print(type(var_set))

### Set - множина унікальних даних (містить унікальні дані)
var_set2 = {1, 2, 3, 4}
print(var_set2)
print(type(var_set2))

var_set3 = {'a', 'c', 'd', 'f'}
print(var_set3)


## Доступ до елементів множини

print('a' in var_set3)

for i in var_set3:
    print('t')

print(var_set3.issuperset(var_set2))
print(var_set3.isdisjoint(var_set))


var_set3.add('t')
print(var_set3)


print(var_set3.difference(var_set2))

_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print(_list)

print(len(_list))

counter = 1
temp_var = None

for i in _list:
    print(i)
    if i != temp_var:
        counter = counter + 1
        temp_var = 1

print(counter)

print(len(set(_list)))


print('set3', var_set3, 'set2', var_set2)
print(var_set3.symmetric_difference(var_set2))

print(var_set3.difference(var_set2))