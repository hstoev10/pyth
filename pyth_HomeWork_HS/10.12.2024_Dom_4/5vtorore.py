#Напишете програма, която при въведени тегло и височина определя дали човекът е наднормено тегло,
#нормално тегло или поднормено тегло. Използвайте индекс на маса на тялото (BM)


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Поднормено тегло"
    elif bmi >= 18.5 and bmi < 25:
        return "Нормално тегло"
    else:
        return "Наднормено тегло"

weight = float(input("Моля, въведете теглото си в килограми: "))
height = float(input("Моля, въведете височината си в метри: "))

result = calculate_bmi(weight, height)
print("Вашият ИМТ показва:", result)

