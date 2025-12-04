for number in range (101):
    if number == 5 or number % 3 == 0 or (60 < number < 81):
        continue
    print(number, end = ' ')
