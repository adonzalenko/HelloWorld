last_number = int(input('Введите последнее число ряда: '))

for number in range(last_number+1):
    if number >= 2:
        if number == 2 or number == 3 or (number % 2 != 0 and number % 3 != 0):
            print(number, end = ' ')


