# напишете програма, която при въведена дължина на страницата на триъгълника проверява 
#дали той е възложен и ако е дали е правоъгълник

# Въвеждане на страни от потребителя
a = float(input("Въведете дължина на страна a: "))
b = float(input("Въведете дължина на страна b: "))
c = float(input("Въведете дължина на страна c: "))


# Проверка за възможност за триъгълник
if a + b > c and a + c > b and b + c > a:
    print("Това е възможен триъгълник.")
    
    # Проверка за правоъгълен триъгълник
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Триъгълникът е правоъгълен.")
    else:
        print("Триъгълникът не е правоъгълен.")
else:
    print("Това не е възможен триъгълник.")

