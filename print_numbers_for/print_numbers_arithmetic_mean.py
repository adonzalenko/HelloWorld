first_number = int(input('Введите первое число: '))
last_number = int(input('Введите последнее число: '))
numbers_sum = 0
i = 0

for number in range(first_number, last_number+1):
    numbers_sum = numbers_sum + number
    i+=1

print(numbers_sum / i)