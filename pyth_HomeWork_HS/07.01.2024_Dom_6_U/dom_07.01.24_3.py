# 3. Напишите програма, която получава последователност от цели числа, разделени от празно 
# място (single space).Принтирайте лист само от четните числа (even numbers). Използвайте filter().

def is_even(number):
    return number % 2 == 0

input_sequence = input("Enter the numbers separated by a space: ")
numbers = list(map(int, input_sequence.split()))
even_numbers = list(filter(is_even, numbers))

print("Even numbers:", even_numbers)
