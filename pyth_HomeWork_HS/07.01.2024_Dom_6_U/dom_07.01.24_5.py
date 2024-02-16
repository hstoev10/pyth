# 5. Напишите програма, която получава лист от цели числа, разделени от празно място (single space).
# Принтирайте минималната и максималната стойност на дадените числа, както и сумата на всички 
# цели числа от листа.
# - "The minimum number is {minimum number}“
# - "The maximum number is {maximum number}“
# - "The sum number is: {sum of all numbers}“
# Използвайте min(), max() и sum().

input_sequence = input("Enter a space-separated list of integers: ")

numbers = list(map(int, input_sequence.split()))

minimum_number = min(numbers)
maximum_number = max(numbers)
sum_of_numbers = sum(numbers)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_numbers}")
