

entered_year = int(input("Введите год для проверки: "))
leap_year = entered_year % 4 == 0 and (entered_year % 100 != 0 or entered_year % 400 == 0)

if entered_year <= 0:
    print("Введите корректный год")
    exit()

if leap_year:
    print("Введенный год високосный")
else:
    print("Введенный год не високосный")
