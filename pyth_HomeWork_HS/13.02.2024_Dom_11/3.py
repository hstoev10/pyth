#  3. Задача. Insertion Sort: Създайте функция, която използва алгоритъма
# Insertion Sort за сортиране на масив от числа. 

def insertion_sort(arr):
    n = len(arr)

    # Проходим през всички елементи в списъка (от първия до последния)
    for i in range(1, n):
        current_element = arr[i]
        j = i - 1

        # Преместваме елементите, по-големи от текущия, на една позиция напред
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Поставяме текущия елемент на правилната позиция в сортирания подсписък
        arr[j + 1] = current_element

# Тестване на алгоритъма със списък от цели числа
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Несортиран списък:", my_list)

insertion_sort(my_list)

print("Сортиран списък:", my_list)
