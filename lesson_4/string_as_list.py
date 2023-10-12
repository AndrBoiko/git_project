var = 'sadfsdfasdfasdfadsf'

print(var[0])
print(var[10])


print(type(var))

_list = list(var)
print(_list)
print(type(_list))

print(_list.count('s'))
print(_list)


# Slicing

print(var[3:7])
print(_list[3:7])
print(_list[:])
print(_list[3:]) #from the elemet to the end
print(_list[:7]) # from beginning to element 6
print(_list[-1]) # last element
print(_list[-2])
print(_list[::-1])
print(_list.reverse())
print(_list)

print(var[::-1])
reversed(_list)
print(_list)

print(_list[-6:])