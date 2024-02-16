# 4. Напишите програма, която получава последователност от цели числа, разделени от 
# празно място (single space).Принтирайте сортиран (sorted) лист от числа във възходящ 
# ред (ascending order).Използвайте sorted().

input_sequence = input("Enter a sequence of space-separated integers: ")

numbers = list(map(int, input_sequence.split()))
sorted_numbers = sorted(numbers)

print("Sorted sheet in ascending order:", sorted_numbers)
