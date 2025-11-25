import math

place_x1 = float(input("Введите координату оси X первой точки угла треугольника: "))
place_y1 = float(input("Введите координату оси Y первой точки угла треугольника: "))
place_x2 = float(input("Введите координату оси X второй точки угла треугольника: "))
place_y2 = float(input("Введите координату оси Y второй точки угла треугольника: "))
place_x3 = float(input("Введите координату оси X третьей точки угла треугольника: "))
place_y3 = float(input("Введите координату оси Y третьей точки угла треугольника: "))

length_a = math.sqrt((place_x2 - place_x1) ** 2 + (place_y2 - place_y1) ** 2)
length_b = math.sqrt((place_x3 - place_x2) ** 2 + (place_y3 - place_y2) ** 2)
length_c = math.sqrt((place_x3 - place_x1) ** 2 + (place_y3 - place_y1) ** 2)

half_meter = (length_a + length_b + length_c) / 2
triange_area = math.sqrt(half_meter * (half_meter - length_a) * (half_meter - length_b) * (half_meter - length_c))

print(f"Площадь треугольника = {triange_area:.2f} см^2")