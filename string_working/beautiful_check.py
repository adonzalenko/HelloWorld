#работа со строками, форматирование, приведение формата к образцу
product = str(input())
cost = int(input())
weight = int(input())
money = int(input())

cash = cost * weight
change = int(money - cash)
weight_cost = f'{weight}кг * {cost}руб/кг'

if change >= 0:
    print(f'{"Чек":=^35}')
    print(f'Товар:{product:>29}')
    print(f'Цена:{weight_cost:>30}')
    print(f'Итого:{cash:>26}руб')
    print(f'Внесено:{money:>24}руб')
    print(f'Сдача:{change:>26}руб')
    print(f'=' * 35)

else:
    print('Недостаточно денег для оплаты')