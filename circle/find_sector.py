import math

radius = 10
sector_angle = 20

area_sector = (math.pi * radius ** 2 * sector_angle) / 360

print(f'Площадь сектора круга с радиусом {radius:.2f} см. и '
      f'углом сектора круга {sector_angle:.2f} град.: {area_sector:.2f} см^2.')
