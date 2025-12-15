
number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
command_number = float(input("Введите номер команды: "))

epsilon = 1e-10

match command_number:
    case 1:
        print(f'{number_1} + {number_2} = {number_1 + number_2:.2f}')
    case 2:
        print(f'{number_1} - {number_2} = {number_1 - number_2:.2f}')
    case 3:
        print(f'{number_1} * {number_2} = {number_1 * number_2:.2f}')
    case 4 if abs(number_2) > epsilon:
        print(f'{number_1} / {number_2} = {number_1 / number_2:.2f}')
    case 4 if abs(number_2) <= epsilon:
        print("Деление на 0 невозможно")
    case _:
        print("Неизвестная операция")