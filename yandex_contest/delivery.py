storage = int(input())
shop = int(input())
speed = int(input())

distance = shop - storage
time = float(distance / speed)

print(f'{time:.2f}')