# 1. Задача. Сортиране Bubble Sort: Имплементирайте алгоритъм за Bubble
# Sort и тествайте със списък от цели числа.

def bubble_sort(arr):
    n = len(arr)

   
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Несортиран списък:", my_list)

bubble_sort(my_list)

print("Сортиран списък:", my_list)
