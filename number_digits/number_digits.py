number_for_work = str(input('Введите число: '))
sum_of_digits = 0
sum_of_digits_not_even = 0
max_numbers = 0

numbers_length = len(number_for_work)
i = 0

while i < numbers_length:
    digit = int(number_for_work[i])
    sum_of_digits += digit

    if digit % 2 != 0:
        sum_of_digits_not_even += digit

    if max_numbers  < digit:
        max_numbers = digit

    i += 1

print(f'Сумма нечетных чисел = {sum_of_digits_not_even}')
print(f'Сумма чисел = {sum_of_digits}')
print(f'Максимальное число = {max_numbers}')
