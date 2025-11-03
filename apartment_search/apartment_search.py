# Найти расположение квартиры в доме, если известно кол-во этажей и подъездов,
# А также, номер квартиры, и как квартиры располагаются на площадке

import math

entrances_count = int(input("Введите количество подъездов в доме: "))
floor_count = int(input("Введите количество этажей в доме: "))
apartment_number = int(input("Введите номер искомой квартиры: "))

if entrances_count < 0 or floor_count < 0 or apartment_number < 0:
    print('Нельзя вводить отрицательное число')
    exit()

apartment_per_floor_number = 4
total_apartments = entrances_count * floor_count * apartment_per_floor_number

if apartment_number > total_apartments:
    print("Квартиры с таким номером нет в доме")
    exit()

count_apartments_in_entrance = floor_count * apartment_per_floor_number
entrance_number = int(math.ceil(apartment_number / count_apartments_in_entrance))
floor_number = math.ceil((apartment_number % count_apartments_in_entrance)
                         / apartment_per_floor_number)
location = ((apartment_number % count_apartments_in_entrance)
            % apartment_per_floor_number)

if location == 1:
    location = "Ближняя слева"
elif location == 2:
    location = "Дальняя слева"
elif location == 3:
    location = "Дальняя справа"
else:
    location = "Ближняя справа"

print("Номер подъезда:", entrance_number)
print("Номер этажа:", floor_number)
print("Положение квартиры на площадке:", location)