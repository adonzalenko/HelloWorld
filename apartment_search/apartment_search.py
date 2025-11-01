#найди расположение квартиры в доме, если известно кол-во этажей и подъездов
#а также номер квартиры, и как квартиры располагаются на площадке

import math

entrances_sum = int(input("Введите количество подъездов в доме: "))
floor_sum = int(input("Введите количество этажей в доме: "))
apartment_number = int(input("Введите номер искомой квартиры: "))

total_apartments = entrances_sum * floor_sum * 4

if apartment_number > total_apartments:
    print("Квартиры с таким номером нет в доме")
    exit()

sum_apartments_in_entrance = int(floor_sum * 4)
entrances_number = int(math.ceil(apartment_number / sum_apartments_in_entrance))
floor_number = math.ceil((apartment_number % sum_apartments_in_entrance)/4)
location = (apartment_number % sum_apartments_in_entrance) % 4

if location == 1:
    location = "Ближняя слева"

if location == 2:
    location = "Дальняя слева"

if location == 3:
    location = "Дальняя справа"

else:
    location = "Ближняя справа"

print("Номер подъезда:", entrances_number)
print("Номер этажа:", floor_number)
print("Положение квартиры на площадке:", location)