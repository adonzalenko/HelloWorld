degree_of_c = float(input("Введите температуру по шкале Цельсия: "))
def get_temperature_of_f(degree_of_c):
    return degree_of_c * 1.8 + 32

def get_temperature_of_k(degree_of_c):
    return degree_of_c + 273.15

print(f'Введенная температура по шкале Фаренгейта: {get_temperature_of_f(degree_of_c):.2f}')
print(f'Введенная температура по шкале Кельвина: {get_temperature_of_k(degree_of_c):.2f}')
