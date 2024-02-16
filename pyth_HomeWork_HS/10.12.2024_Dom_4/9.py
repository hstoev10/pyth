#Напишете програма, която изчислява факториела на въведено число

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

number = int(input("Въведете число: "))
result = calculate_factorial(number)
print(f"{number}! = {result}")
