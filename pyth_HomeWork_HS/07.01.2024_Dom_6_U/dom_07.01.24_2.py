# 2. Напишите програма, която ще получава три цели числа от тип int. Направете следните функции:
# • sum_numbers(), която ще връща return сборът на първите две цели числа.
# • substract(), която ще връща разликата от върнатата стойност на първите две цели числа и третото
# число.Обединете двете функции в една главна с име add_and_subtract(), която ще получава трите цели 
# числа като параметри.Принтирайте резултата на функцията subtract() на конзолата.

def sum_numbers(a, b):
    return a + b

def subtract(x, y, z):
    return x - y - z

def add_and_subtract(num1, num2, num3):
    total_sum = sum_numbers(num1, num2)
    result = subtract(total_sum, num3, 0)
    return result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

result = add_and_subtract(num1, num2, num3)
print(f"The difference of the sum of the first two numbers and the third number is: {result}")
