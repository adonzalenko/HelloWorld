day = int(input("Введите сегодняшний день: "))
month = int(input("Введите сегодняшний месяц: "))
year = int(input("Введите сегодняшний год: "))

if day >31 or day <1 or month >12 or month <1 or year <1:
    print("Введите корректную дату")
    exit()

next_day = day + 1
check_year = year % 4

if month == 2:
    if check_year == 0:
        if next_day > 29:
            next_day = next_day - 29
            next_month = month + 1
            next_year = year
        else:
            if next_day > 28:
                next_day = next_day - 28
                next_month = month + 1
                next_year = year


                # if month == 2 and check_year == 0 and next_day > 29:
                #     next_day = next_day - 29
                #     next_month = month + 1
                #     next_year = year
                # elif month == 2 and check_year != 0 and next_day > 28:
                #     next_day = next_day - 28
                #     next_month = month + 1
                #     next_year = year
elif next_month > 12:
        next_month = next_month - 12
        next_year = year + 1
else:
    if month == 1 or 3 or 5 or 7 or 8 or 10:
        if next_day > 31:
            next_day = next_day - 31
            next_month = month + 1
        else:
            next_month = month
            next_year = year
    else:
        if next_day > 30:
            next_day = next_day - 30
            next_month = month + 1

print(f"{next_day:02}.{next_month:02}.{next_year}")
