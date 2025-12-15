x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))


def get_minimus(x, y):
    if x < y:
        minimus = x
    else:
        minimus = y
    return minimus


def get_maximus(x, y):
    if x < y:
        maximus = y
    else:
        maximus = x
    return maximus


print(f'Максимальное число = {get_maximus(x,y)}, Минимальное число = {get_minimus(x,y)}')