#Напишете програма, която конвертира температура от Целзий във Фаренхайт или
#обратното, според избора на потребителя

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Избор на потребителя
choice = input("Изберете опция:\n1. Конвертиране от Целзий във Фаренхайт\n2. Конвертиране от Фаренхайт в Целзий\n")

# Проверка на валидност на избора
if choice in ['1', '2']:
    # Въвеждане на температурата от потребителя
    temperature = float(input("Въведете температурата: "))

    # Извършване на конверсията според избора
    if choice == '1':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature:.2f} Целзий е {result:.2f} Фаренхайт.")
    else:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature:.2f} Фаренхайт е {result:.2f} Целзий.")
else:
    print("Невалиден избор. Моля, изберете 1 или 2.")
