i = 1

while i <= 100:
    if i == 5 or i % 3 == 0 or (60 < i < 81):
        i += 1
        continue
    print(i, end = ' ')
    i += 1