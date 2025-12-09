from unicodedata import digit

number_for_work = str(input('Введите число: '))
sum_of_digits = 0
sum_of_digits_not_even = 0
max_numbers = 0
numbers_length = len(number_for_work)
i = 0
j = 0
m = 0

while i < numbers_length:
    sum_of_digits += int(number_for_work[i])
    i += 1
print(f'Сумма чисел = {sum_of_digits}')

while j < numbers_length:
    if int(number_for_work[j]) % 2 != 0:
        sum_of_digits_not_even += int(number_for_work[j])
    j += 1
print(f'Сумма нечетных чисел = {sum_of_digits_not_even}')

while m < numbers_length:
    if max_numbers  < int(number_for_work[m]):
        max_numbers = int(number_for_work[m])
    m += 1
print(f'Максимальное число = {max_numbers}')
