# Створити пустий словник
empty_dict = {}

# Створити новий словник з парами ключ:значення
my_dict = {"ім'я": "Анна", "вік": 25, "місто": "Київ"}

# Додати одну пару ключ:значення до першого словника
empty_dict["країна"] = "Україна"

# Додати до першого словника другий словник використовуючи .update()
empty_dict.update(my_dict)

# Видалити один елемент словника за допомогою .pop()
age = empty_dict.pop("вік")

# Видалити один елемент за допомогою .popitem()
item = empty_dict.popitem()

# Зробити глибоку копію першого словника в нову змінну
deep_copy_dict = empty_dict.copy()

# Додати до нового словника новий ключ, а як значення передати перший словник
deep_copy_dict["перший словник"] = empty_dict

# Вивести список ключів
keys = list(empty_dict.keys())

# Вивести список значень
values = list(empty_dict.values())

# Виведення результатів
print(empty_dict)
print(my_dict)
print(age)
print(item)
print(deep_copy_dict)
print(keys)
print(values)

# Створити перший set
set1 = {1, 2, 3, 4, 5, 6, 7}

# Створити другий set
set2 = {5, 6, 7, 8, 9, 10, 11}

# Розширити перший set за допомогою .add(0)
set1.add(0)

# Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент
intersection_result = set1.intersection(set2)

# Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент
difference_result = set1.difference(set2)

# Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент
symmetric_difference_result = set1.symmetric_difference(set2)

# Вивести всі змінні у консоль
print(set1)
print(set2)
print(intersection_result)
print(difference_result)
print(symmetric_difference_result)

# Створення кортежу
my_tuple = (1, 2, 3, 4, 5, 6, 7)

# Виведення кортежу в консоль
print(my_tuple)

# Створення кортежу кортежів
tuple_of_tuples = ((1, 2), (3, 4), (5, 6))

# Виведення кортежу кортежів в консоль
print(tuple_of_tuples)

# Початковий кортеж
initial_tuple = (1, 2, 3)

# Створення списку
my_list = [4, 5, 6]

# Розширення кортежу через приведення типів
extended_tuple = tuple(initial_tuple) + tuple(my_list)

# Виведення розширеного кортежу в консоль
print(extended_tuple)
