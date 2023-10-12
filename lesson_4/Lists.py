import copy

_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

_list2 = [1, 2, 'three']

_list3 = [_list, _list2]

print(_list)
print(_list2)
print(_list3)

print(len(_list))
print(len(_list2))
print(len(_list3))

print(_list3[0])

print(id(_list))
print(id(_list3[0]))

# Copying the lists
_shallow_copy = _list

print(id(_shallow_copy))
print(_shallow_copy)

print(id(_list))
print(_list)

_hard_copy = _list.copy()
print(id(_hard_copy))
print(_hard_copy)

print(id(_list))
print(_list)


## Deep copy

_hard_copy_list = copy.copy(_list3)
_deep_copy = copy.deepcopy(_list3)

print(id(_hard_copy_list))
print(id(_hard_copy_list[0]))


### Lists

print(_list[3])

print(_list.count(5))

print(_list.sort(reverse=True))
print(_list)
print(_list.extend(_list2))
print(_list)
print(_list.append(_list2))
print(_list)

_list.insert(9,0)
print(_list)

print(_list.pop(0))


