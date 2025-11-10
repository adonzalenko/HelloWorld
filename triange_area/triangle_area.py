import math

place_x1 = float(input("Введите координату оси X первой точки угла треугольника: "))
place_y1 = float(input("Введите координату оси Y первой точки угла треугольника: "))
place_x2 = float(input("Введите координату оси X второй точки угла треугольника: "))
place_y2 = float(input("Введите координату оси Y второй точки угла треугольника: "))
place_x3 = float(input("Введите координату оси X третьей точки угла треугольника: "))
place_y3 = float(input("Введите координату оси Y третьей точки угла треугольника: "))

lenght_a = math.sqrt((math.fabs(place_x2-place_x1)) ** 2 + (math.fabs(place_y2-place_y1)) ** 2)
lenght_b = math.sqrt((math.fabs(place_x3-place_x2)) ** 2 + (math.fabs(place_y3-place_y2)) ** 2)
lenght_c = math.sqrt((math.fabs(place_x3-place_x1)) ** 2 + (math.fabs(place_y3-place_y1)) ** 2)

half_meter = (lenght_a + lenght_b + lenght_c) / 2
triange_area = math.sqrt((half_meter) * (half_meter - lenght_a) * (half_meter - lenght_b) * (half_meter - lenght_c))

print(f"Площадь треугольника = {triange_area:.2f} см^2")