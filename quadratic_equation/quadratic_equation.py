from math import sqrt

ratio_a = float(input("<Введите коэффициент а: "))
ratio_b = float(input("<Введите коэффициент b: "))
ratio_c = float(input("<Введите коэффициент c: "))

if ratio_a == 0:
    if ratio_c == 0:
        print("Любое число является решением")
    else:
        if ratio_b != 0:
            equation_solving = -ratio_c / ratio_b
            print(f"Корень уравнения = {equation_solving}")
        else:
            print("Уравнение неразрешимо")
elif ratio_b == 0:
    if ratio_a != 0:
        if ratio_c >= 0:
            equation_solving_2 = sqrt(-ratio_c / ratio_a)
            print(f"Корень уравнения =+- {equation_solving_2}")
        else:
            print("Реальный корней нет")
    else:
        print("Коэффициент а не может быть равен 0")
else:
    result_d = ratio_b ** 2 - (4 * ratio_a * ratio_c)
    if result_d < 0:
        print("Корней нет")
    elif result_d == 0:
        equation_root = -ratio_b / (2 * ratio_a)
        print(f"Корень уравнения = {equation_root:.2f} ")
    else:
        equation_root_1 = (-ratio_b + sqrt(result_d)) / (2 * ratio_a)
        equation_root_2 = (-ratio_b - sqrt(result_d)) / (2 * ratio_a)
        print(f"Корень уравнения 1 = {equation_root_1:.2f}")
        print(f"Корень уравнения 2 = {equation_root_2:.2f}")