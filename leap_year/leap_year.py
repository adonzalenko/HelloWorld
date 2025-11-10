from math import remainder

entered_year = int(input("Введите год для проверки: "))
entered_year_remainder = remainder(entered_year, 4)

if entered_year <= 0:
    print("Введите корректный год")
    exit()

if entered_year_remainder == 0:
    print("Введенный год високосный")
else:
    print("Введенный год не високосный")
