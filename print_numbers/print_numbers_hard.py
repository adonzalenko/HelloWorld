first_number = int(input('Введите начальное число: '))
last_number = int(input('Введите конечное число: '))
n = int(input('Введите количество чисел в ряду: '))

i = first_number
k = len(str(last_number)) + 1
count_in_current_row = 0

while i <= last_number:
    if count_in_current_row >= n:
        print()
        count_in_current_row = 0

    print(f'{i:>{k}}', end = '')
    i += 1
    count_in_current_row += 1
