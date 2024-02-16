# 2. Сума на Числа: Създайте рекурсивна функция, която намира
# сумата на всички цели числа от 1 до n.

def sum_numbers(n):
    if n <= 0:
        return "Невалиден вход. n трябва да бъде по-голямо от 0."
    elif n == 1:
        return 1
    else:
        return n + sum_numbers(n-1)

# Пример за извикване на функцията с n = 5
result = sum_numbers(5)
print(result)
