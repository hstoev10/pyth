# 6. Използване на библиотеката random
# за генериране на случайни числа:
# Задача: Използвайте random за генериране на
# 5 случайни числа между 1 и 10 и ги отпечатайте.

import random

# Генериране на 5 случайни числа между 1 и 10
random_numbers = [random.randint(1, 10) for _ in range(5)]

# Отпечатване на генерираните числа
print("Случайни числа:", random_numbers)
