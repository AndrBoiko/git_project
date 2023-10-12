var_dict = {}
var_dict1 = dict()

print(var_dict)
print(var_dict1)
print(type(var_dict))
print(type(var_dict1))

var_dict2 = {
    'key': 'value'
}
print('One time', var_dict2)

var_dict3 = {
    '1': 10,
    '2': 20,
    '3': 30
}
print('Multi', var_dict3)

print(var_dict3['1'])
print(type(var_dict3['1']))

print(var_dict3.setdefault(True))

print(var_dict3.items())


