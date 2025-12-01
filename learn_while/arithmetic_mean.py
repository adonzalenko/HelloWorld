number_begin = float(input("Введите начало диапазона: "))
number_end = float(input("Введите начало диапазона: "))

i = number_begin
numbers_sum = 0
numbers_sum_ever_only = 0
k = 0
n = 0

while i <= number_end:
    if i % 2 == 0:
        numbers_sum_ever_only += i
        n = n + 1
    numbers_sum += i
    i += 1
    k = k + 1

arithmetic_mean = numbers_sum / k
print(f'Среднее арифметическое чисел из диапазона от {number_begin} по {number_end} = {arithmetic_mean:.2f}')

arithmetic_mean_new = numbers_sum_ever_only / n
print(f'Среднее арифметическое только четных чисел из диапазона от {number_begin} по {number_end} = {arithmetic_mean_new:.2f}')
