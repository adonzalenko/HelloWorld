i = 3
numbers_sum = 0
k = 0

while i <= 21:
    if i % 2 == 0:
        numbers_sum = numbers_sum + i
        k = k + 1
    i = i + 1

print("Сумма чисел = " + str(numbers_sum))
print("Количество четных чисел = " + str(k))