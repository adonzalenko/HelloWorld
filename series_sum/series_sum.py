last_number = int(input('Введите последнее число ряда: '))

i = 1
series_sum = 0
series_sum_even = 0

while i <= last_number:
    if i % 2 == 0:
        series_sum_even = series_sum_even + i ** 2
    else:
        series_sum = series_sum + i ** 2
    i += 1

total_sum = series_sum - series_sum_even
print(f'Итоговая сумма = {total_sum}')
