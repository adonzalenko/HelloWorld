number_begin = float(input("Введите начало диапазона: "))
number_end = float(input("Введите начало диапазона: "))

i = number_begin
numbers_sum = 0
even_numbers_sum = 0
number_of_numbers = 0
number_of_even_numbers = 0

while i <= number_end:
    if i % 2 == 0:
        even_numbers_sum += i
        number_of_even_numbers = number_of_even_numbers + 1

    numbers_sum += i
    i += 1
    number_of_numbers = number_of_numbers + 1

arithmetic_mean = numbers_sum / number_of_numbers
print(f'Среднее арифметическое чисел из диапазона от {number_begin} по {number_end} = {arithmetic_mean:.2f}')

arithmetic_mean_new = even_numbers_sum / number_of_even_numbers
print(f'Среднее арифметическое только четных чисел из диапазона от {number_begin} по {number_end} = {arithmetic_mean_new:.2f}')
