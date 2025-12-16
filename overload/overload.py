def get_type_name(argument):
    if isinstance(argument, int):
        return 'Целое число'
    elif isinstance(argument, float):
        return 'Вещественное число'
    elif isinstance(argument, complex):
        return 'Комплексное число'
    elif isinstance(argument, str):
        return 'Строка'
    elif argument(argument, bool):
        return 'Логическое значение'
    else:
        return 'Неизвестный тип'

print(get_type_name('Привет'))
print(get_type_name(2.5))
print(get_type_name(False)) #неправильно работает тип bool
print(get_type_name(4))

#TODO По уссловия задачи требуется решить задачи с помощью multiple dispatch, но такой библиотеки нет