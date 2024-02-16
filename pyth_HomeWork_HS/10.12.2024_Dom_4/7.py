#Напишете програма, която изчислява средното аритмитично и медианата
#от три въведени числа

def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

def calculate_median(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    median = numbers[1]  # Средното число в сортирания списък
    return median

# Въвеждане на три числа от потребителя
num1 = float(input("Въведете първото число: "))
num2 = float(input("Въведете второто число: "))
num3 = float(input("Въведете третото число: "))

# Изчисляване на средното аритметично и медианата
average = calculate_average(num1, num2, num3)
median = calculate_median(num1, num2, num3)
print(f"Средното аритметично е: {average:.2f}")
print(f"Медианата е: {median:.2f}")

