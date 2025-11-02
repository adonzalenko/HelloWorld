# работа со строками, форматирование, приведение формата к образцу
product = str(input("Введите название продукта: "))
cost = float(input("Введите стоимость продукта: "))
weight = float(input("Введите вес продукта: "))
money = float(input("Введите размер внесенных средств: "))

cash = cost * weight
change = float(money - cash)
weight_cost = f'{weight}кг * {cost}руб/кг'

if change < 0:
    print('Недостаточно денег для оплаты')
else:
    print(f'{"Чек":=^35}')
    print(f'Товар:{product:>29}')
    print(f'Цена:{weight_cost:>30}')
    print(f'Итого:{cash:>26}руб')
    print(f'Внесено:{money:>24}руб')
    print(f'Сдача:{change:>26}руб')
    print(f'=' * 35)