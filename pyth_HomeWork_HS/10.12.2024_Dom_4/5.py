#Напишете програма, която при въведени тегло и височина определя дали човекът е наднормено тегло,
#нормално тегло или поднормено тегло. Използвайте индекс на маса на тялото (BM)

def calculate_bmi(weight, height):
    # Преобразуване на височината от сантиметри в метри
    height_in_meters = height / 100.0
    
    # Изчисляване на индекса на маса на тялото (BMI)
    bmi = weight / (height_in_meters ** 2)
    return bmi

def determine_weight_status(bmi):
    if bmi < 18.5:
        return "Поднормено тегло"
    elif 18.5 <= bmi < 25:
        return "Нормално тегло"
    else:
        return "Наднормено тегло"

# Въвеждане на тегло и височина от потребителя
weight = float(input("Въведете тегло в килограми: "))
height = float(input("Въведете височина в сантиметри: "))

# Изчисляване на BMI и определяне на статуса на теглото
bmi = calculate_bmi(weight, height)
weight_status = determine_weight_status(bmi)

# Извеждане на резултата
print(f"Вашият BMI е: {bmi:.2f}")
print(f"Статус на теглото: {weight_status}")
