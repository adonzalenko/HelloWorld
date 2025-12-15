def get_order_cost(number_product_1, number_product_2, cost_product_1, cost_product_2):
    if ((number_product_1 + number_product_2) < 10 and
             (number_product_1 * cost_product_1 + number_product_2 * cost_product_2) < 1000):
        order_cost = (number_product_1 * cost_product_1 + number_product_2 * cost_product_2) * 0.90


    elif ((number_product_1 + number_product_2) < 10 or
           (number_product_1 * cost_product_1 + number_product_2 * cost_product_2) < 1000):
        order_cost  = (number_product_1 * cost_product_1 + number_product_2 * cost_product_2) * 0.95


    else:
        order_cost = number_product_1 * cost_product_1 + number_product_2 * cost_product_2

    return order_cost

print(f"Итоговая стоимость заказа с учетом скидки: {get_order_cost(40, 90, 100, 105):.2f}")
