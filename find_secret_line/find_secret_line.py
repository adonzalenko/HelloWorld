secret_line = 'hello world'
line = str(input('Введите строку для разгадывания: '))

while True:
    if line == secret_line:
        print('Вы угадали секретную строку!')
        break
    line = str(input('Введите строку для разгадывания: '))

