number1 = int(input("Введите целое число 1: "))
number2 = int(input("Введите целое число 2: "))

max = number1 if number1 > number2 else number2
min = number1 if number1 < number2 else number2

print(f"Максимальное число = {max}, минимальное число = {min}")