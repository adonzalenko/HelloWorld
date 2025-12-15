# def only_even(numbers):
#     for x in numbers:
#         if x % 2 != 0:
#             return False
#     return True
#
# print(only_even([2, 4, 6]))
# print(only_even([1, 2, 3]))
#


# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True
#
# print(only_even([2, 4, 6]))
# print(only_even([1, 2, 3]))

def f(count):
    count += 1
    print(f'Количество вызовов функции равно {count}.')
    return count

count_f = 0
count_f = f(count_f)
count_f = f(count_f)
count_f = f(count_f)



