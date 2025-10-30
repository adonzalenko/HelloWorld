#Сегодня в N часов M минут владелец магазина заказал доставку нового товара
#оператор сообщил, что товары доставят через Т минут
#сколько времени будет на эл часах, когда привезут продукты?
# Ввод в виде:
#N -целое число
#M - целое число
#T - целое число
#Вывод в виде: 08:05
#проверка пула

n = int(input())
m = int(input())
t = int(input())

days = t // 1440
hours = t // 60 - 24 * days

result_hours = n + hours
result_minutes = m + (t - t // 60 * 60)

if result_hours > 24:
    result_hours = result_hours - 24

if result_minutes > 60:
    result_minutes = result_minutes - 60
    result_hours = result_hours + 1

    print(f'{result_hours:0>2}:{result_minutes:0>2}')

else:
    print(f'{result_hours:0>2}:{result_minutes:0>2}')
