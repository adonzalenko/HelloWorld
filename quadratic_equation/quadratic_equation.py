from math import sqrt
from math import fabs

ratio_a = float(input("<Введите коэффициент а: "))
ratio_b = float(input("<Введите коэффициент b: "))
ratio_c = float(input("<Введите коэффициент c: "))

epsilon = 1.0e-10

if fabs(ratio_a) < epsilon:
    if fabs(ratio_b) < epsilon:
        if fabs(ratio_c) < epsilon:
            print("Любое число является решением")
        else:
            print("Уравнение неразрешимо")
    else:
        equation_solving = -ratio_c / ratio_b
        print(f"Корень уравнения = {equation_solving}")
else:
    result_d = ratio_b ** 2 - 4 * ratio_a * ratio_c
    if result_d <= -epsilon:
        print("Корней нет")
    elif fabs(result_d) < epsilon:
        equation_root = -ratio_b / (2 * ratio_a)
        print(f"Корень уравнения = {equation_root:.2f} ")
    else:
        equation_root_1 = (-ratio_b + sqrt(result_d)) / (2 * ratio_a)
        equation_root_2 = (-ratio_b - sqrt(result_d)) / (2 * ratio_a)
        print(f"Корень уравнения 1 = {equation_root_1:.2f}")
        print(f"Корень уравнения 2 = {equation_root_2:.2f}")