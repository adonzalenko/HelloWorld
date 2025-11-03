# найти вес каждой из двух партий котлет, если известны следующие параметры:

total_weight = float(input('Введите общий вес котлет: '))
average_cost = float(input('Введите стоимость котлет за кг.: '))
first_batch_cost = float(input('Введите стоимость первого вида котлет за кг.: '))
second_batch_cost = float(input('Введите стоимость второго вида котлет за кг.: '))

total_cost = total_weight * average_cost  # Общая стоимость двух партий

if first_batch_cost == second_batch_cost:  # если стоимость котлет одинаковая
    first_batch_weight = second_batch_weight = total_weight // 2
elif first_batch_cost > second_batch_cost:
    second_batch_weight = (total_cost - total_weight * first_batch_cost) / (
                second_batch_cost - first_batch_cost)  # расчет веса второй партии котлет
    first_batch_weight = total_weight - second_batch_weight  # расчет веса первой партии котлет
else:
    first_batch_weight = (total_cost - total_weight * second_batch_cost) / (
                first_batch_cost - second_batch_cost)  # расчет веса первой партии котлет
    second_batch_weight = total_weight - first_batch_weight  # расчет веса второй партии котлет

print(f'Вес первой партии котлет {first_batch_weight} кг.')
print(f'Вес второй партии котлет {second_batch_weight} кг.')