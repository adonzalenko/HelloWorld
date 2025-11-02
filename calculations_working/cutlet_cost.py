# найти вес каждой из двух партий котлет, если известны следующие параметры:

total_weight = float(input('Введите общий вес котлет: '))
avarage_cost = float(input('Введите стоимость котлет за кг.: '))
first_batch_cost = float(input('Введите стоимость первого вида котлет за кг.: '))
second_batch_cost = float(input('Введите стоимость второго вида котлет за кг.: '))

C = total_weight * avarage_cost  # Общая стоимость двух партий

if first_batch_cost == second_batch_cost:  # если стоимость котлет одинаковая
    first_batch_weight = second_batch_weight = total_weight // 2
elif first_batch_cost > second_batch_cost:
    second_batch_weight = (C - total_weight * first_batch_cost) / (
                second_batch_cost - first_batch_cost)  # расчет веса второй партии котлет
    first_batch_weight = total_weight - second_batch_weight  # расчет веса первой партии котлет
else:
    first_batch_weight = int((C - total_weight * second_batch_cost) / (
                first_batch_cost - second_batch_cost))  # расчет веса первой партии котлет
    second_batch_weight = int(total_weight - first_batch_weight)  # расчет веса второй партии котлет

print(f'Вес первой партии котлет {first_batch_weight} кг.')
print(f'Вес второй партии котлет {second_batch_weight} кг.')