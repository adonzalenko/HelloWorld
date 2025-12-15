first_number = int(input('Введите начальное число: '))
last_number = int(input('Введите конечное число: '))
number_of_numbers = int(input('Введите количество чисел в ряду: '))

i = first_number
line_length = len(str(last_number)) + 1
count_in_current_row = 0

while i <= last_number:
    if count_in_current_row >= number_of_numbers:
        print()
        count_in_current_row = 0

    print(f'{i:>{line_length}}', end ='')
    i += 1
    count_in_current_row += 1
