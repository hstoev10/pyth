# 4. Задача. Binary search. Имлементирайте Binary search алгоритъм за
# намиране дали дадено число съществува в даден лист. За целта си
# създайте масив от 100 елемента със случайни числа и друго
# случайно число, което да търсите в масива.

import random

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

my_array = sorted([random.randint(1, 1000) for _ in range(100)])
target_number = random.randint(1, 1000)

print("Масив:", my_array)
print("Търсено число:", target_number)

if binary_search(my_array, target_number):
    print(f"{target_number} се съдържа в масива.")
else:
    print(f"{target_number} не се съдържа в масива.")
