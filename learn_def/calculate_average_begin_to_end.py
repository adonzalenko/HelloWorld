def get_numbers_average(begin, end):
    numbers_sum = 0
    numbers_count = 0
    for number in range(begin, end+1):
        numbers_sum += number
        numbers_count += 1
        number += 1
    return numbers_sum / numbers_count

print(get_numbers_average(1, 10))