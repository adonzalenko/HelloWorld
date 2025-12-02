password = "Hello123"
new_password = str(input("Введите новый пароль: "))

password_lenght = len(password)
new_password_lenght = len(new_password)

if password == new_password:
    print("Пароль верный")
elif password != new_password and password_lenght == new_password_lenght:
    print("Пароль неверный")
elif password_lenght < new_password_lenght:
    print("Пароль неверный, введенный пароль слишком длинный")
else:
    print("Пароль неверный, введенный пароль слишком короткий")