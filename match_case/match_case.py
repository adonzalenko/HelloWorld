command_execute = input("Введите название команды: ")

match command_execute:
    case "print":
        new_line = input("Введите строку для вывода: ")
        print(f'Вы ввели: {new_line}')
    case "sum":
        number_1 = int(input("Введите число 1: "))
        number_2 = int(input("Введите число 2: "))
        print(number_1 + number_2)
    case other:
        print("Неизвестная команда")
