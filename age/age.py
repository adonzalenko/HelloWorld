age  = int(input("Введите возраст: "))
remains_age = age % 10
exclusion_range = 11 <= age % 100 <= 14

if age < 0:
    print("Введите корректный возраст")
    exit()

if age < 1:
    print("Вы слишком малы")
elif age > 112:
    print("Вы слишком стары")
else:
    if not exclusion_range and (remains_age == 1):
        print(f"Вам {age} год")
    elif not exclusion_range and (remains_age in range(2, 5)):
        print(f"Вам {age} года")
    else:
        print(f"Вам {age} лет")