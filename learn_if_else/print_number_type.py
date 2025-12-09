from math import remainder

number = int(input("Введите целое число: "))

remaining_part_2 = remainder(number, 2)
remaining_part_5 = remainder(number, 5)

if remaining_part_2 == 0 and remaining_part_5 == 0:
    print("Число четное и кратно 5")
elif remaining_part_2 == 0 and remaining_part_5 != 0:
    print("Число четное и не кратно 5")
elif remaining_part_2 != 0 and remaining_part_5 == 0:
    print("Число нечетное и кратно 5")
else:
    print("Число нечетное и не кратно 5")