var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

var_new_list = []
for item in var_list:
    if item % 2 == 0:
        var_new_list.append(item)
print(var_new_list)

var_even_elements = [item for item in var_list if item % 2 == 0]
print(var_even_elements)


var_for_list = []
for x in var_list:
    var_for_list.append(x ** 2)

var_list_example = [1, 2, 3]
