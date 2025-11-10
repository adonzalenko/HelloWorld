age  = int(input("Введите возраст: "))
remains_age = age % 10

if age < 1:
    print("Вы слишком малы")
elif age > 112:
    print("Вы слишком стары")
else:
    if age == 1 or remains_age == 1:
        print(f"Вам {age} год")
    elif 1 < age < 5 or 1 < remains_age < 5:
        print(f"Вам {age} года")
    else:
        print(f"Вам {age} лет")