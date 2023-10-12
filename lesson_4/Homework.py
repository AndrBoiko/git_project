### Рядки:
  ## Навести приклад простого рядка

var = 'Simple string'
print(var)

  ## Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)

multi_var = """
beginnings of poetry
the rice planting songs
of the Interior """
print(multi_var)

  ## Навести приклад рядка з ігноруванням екрануючих символів (Raw)

var_raw = r"C:\Users\MacOS\Andrii"
print(var_raw)

  ## Навести приклад форматування довгих рядків

var_multiline = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
"""
print(var_multiline)

####  Списки

### створити список

_list = [1, 2, 3, 4, 5, 6]
print(_list)

#### копіювати через .copy()

_list2 = [7, 8, 9]
_list2 = _list.copy()
print(_list2)

##### додати елемент до списку

_list2.append(_list)
print(_list2)

### вставити елемент а певне місце.

_list.insert( 7, 8 )
print(_list)

### додати один список до іншого 2 способами

plus_list = _list + _list2
print(plus_list)

_list.extend(_list2)
print(_list)

## команда .pop()

print(_list.pop(3))

print(_list.remove(5))

value = _list[2]
print(_list)

import copy

# Створення посилання на перший список
original_list = [1, 2, [3, 4]]
reference_list = original_list

# Створення поверхової (shallow copy) копії першого списку
shallow_copy = copy.copy(original_list)

# Створення глибокої (повної) (deep copy) першого списку
deep_copy = copy.deepcopy(original_list)

# Виведення значень всіх списків
print("Original List:", original_list)
print("Reference List:", reference_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

# Зміна першого списку
original_list.append(5)
original_list[2].append(6)

# Виведення значень всіх списків після змін
print("\nПісля зміни першого списку:")
print("Original List:", original_list)
print("Reference List:", reference_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

# Створення 3-вимірного списку

three_dimensional_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                          [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                          [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
print(three_dimensional_list)

# Зміна елементу (наприклад, перший елемент у другому списку)

three_dimensional_list[1][0][0] = 100

# Виведення значень після зміни

print(three_dimensional_list)

# Створення словника зі вкладеним списком
my_dict = {
    'назва': 'Приклад словника',
    'список': [1, 2, 3, 4, 5]
}

# Збереження вкладеного списку у нову змінну
nested_list = my_dict['список']

# Виведення змісту словника та вкладеного списку
print("Зміст словника:")
print(my_dict)
print("Вкладений список:")
print(nested_list)

# Використання форматування рядків з допомогою '.format()'
formatted_string = "Назва: {}, Кількість елементів у списку: {}".format(my_dict['назва'], len(my_dict['список']))
print("'.format()':")
print(formatted_string)

# Використання форматування рядків з допомогою 'f'''
formatted_string_f = f"Назва: {my_dict['назва']}, Кількість елементів у списку: {len(my_dict['список'])}"
print("'f''':")
print(formatted_string_f)

# Рядок
my_string = "Hello, World"

# Метод .split() - розбиває рядок на список слів
words = my_string.split()
print(words)

# Методи .upper(), .lower() і .capitalize() - змінюють регістр рядка
upper_case = my_string.upper()
lower_case = my_string.lower()
capitalized = my_string.capitalize()
print( upper_case)
print(lower_case)
print(capitalized)

# Метод .find() - знаходить позицію підстрічки в рядку
position = my_string.find("приклад")
print(position)

# Конструкція [::] - перевернення рядка
reversed_string = my_string[::-1]
print(reversed_string)

# Список
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Перевернути список
reversed_list = my_list[::-1]
print(reversed_list)

# Взяти частину списку від 2 до 7 елементу з кроком 2
subset = my_list[2:8:2]
print(subset)

# Перевернути частину рядка
subset_reversed = my_string[2:8][::-1]
print(subset_reversed)

# Вивести всі елементи списку в консоль за допомогою циклу for
for item in my_list:
    print(item)

# Виведення списку за допомогою циклу while
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

