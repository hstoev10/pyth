# 3. Обръщане на Низ: Напишете рекурсивна функция, която
# обръща даден низ без да използва вградени функции.

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Пример за извикване на функцията с низ "hello"
result = reverse_string("hello")
print(result)
