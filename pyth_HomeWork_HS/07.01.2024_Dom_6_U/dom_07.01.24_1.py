# 1. Напишете функция, която получава три числа (int) и връща (return) най-малкото.
# • Принтирайте резултата на конзолата. Използвайте подходящо име за функцията.

def the_smallest_number(a, b, c):
    return min(a, b, c)

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

result = the_smallest_number(num1, num2, num3)
print(f"The smallest number is: {result}")
