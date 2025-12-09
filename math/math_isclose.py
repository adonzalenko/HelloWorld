import math

number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))

epsilon = 1e-10

if math.isclose(number_1, number_2, abs_tol=epsilon):
    print("Числа равны")
else:
    print("Числа не равны")
