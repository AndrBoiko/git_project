def sum_range(start, end):

    if start > end:
        start, end = end, start


    total = 0


    for num in range(start, end + 1):
        total += num

    return total

start = 5
end = 10
result = sum_range(start, end)
print(f"Сума чисел від {start} до {end} включно: {result}")

def season(month):
    if 1 <= month <= 12:
        if 3 <= month <= 5:
            return "весна"
        elif 6 <= month <= 8:
            return "літо"
        elif 9 <= month <= 11:
            return "осінь"
        else:
            return "зима"
    else:
        return "Невірний номер місяця"

month = 7
result = season(month)
print(f"Місяць {month} належить до пори року: {result}")

def get_filtered(a):
    for item in a:
        if item < 5:
            print(item)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


get_filtered(a)
