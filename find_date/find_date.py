day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

check_year = year % 4

if day >31 or day <1 or month >12 or month <1 or year <1:
    print("Введите корректную дату")
    exit()
elif month == 2:
    if check_year == 0:
        if day > 29:
            print("Введите корректную дату")
            exit()
    else:
        if day > 28:
            print("Введите корректную дату")
            exit()
elif month in [4, 6, 9, 11]:
    if day > 30:
        print("Введите корректную дату")
        exit()
else:
    if day > 31:
        print("Введите корректную дату")
        exit()

next_day = day
next_month = month
next_year = year

if month == 2:
    if check_year == 0:
        if day == 29:
            next_day = 1
            next_month = 3
        else:
            next_day = day + 1
elif month in [4, 6, 9, 11]:
    if day == 30:
        next_day = 1
        next_month = month + 1
    else:
        next_day = day + 1
else:
    if day == 31:
        if month == 12:
            next_day = 1
            next_month = 1
            next_year = year + 1
        else:
            next_day = 1
            next_month = month + 1
    else:
        next_day = day + 1

print(f"Введенная дата: {day:02}.{month:02}.{year}")
print(f"Следующий день: {next_day:02}.{next_month:02}.{next_year}")
