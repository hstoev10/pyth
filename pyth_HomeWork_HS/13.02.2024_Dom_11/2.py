# 2. Задача. Selection Sort: Имплементирайте алгоритъма за сортиране
# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Несортиран списък:", my_list)

selection_sort(my_list)

print("Сортиран списък:", my_list)
