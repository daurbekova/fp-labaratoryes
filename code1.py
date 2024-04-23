import math
from functools import reduce
numbers = [1, 4, 9, 16, 25]
sqrt_numbers = list(map(math.sqrt, numbers))
filtered_sqrt_numbers = list(filter(lambda x: x > 2, sqrt_numbers))
sum_of_filtered_sqrt = reduce(lambda x, y: x + y, filtered_sqrt_numbers)
print("Исходные числа:", numbers)
print("Квадратные корни:", sqrt_numbers)
print("Отфильтрованные квадратные корни (больше 2):", filtered_sqrt_numbers)
print("Сумма отфильтрованных квадратных корней:", sum_of_filtered_sqrt)
