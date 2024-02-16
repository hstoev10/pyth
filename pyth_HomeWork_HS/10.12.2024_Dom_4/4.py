#Напишете програма, която при въведена буква извежда съобщение дали 
#тя е гласна или съгласна

def check_letter_type(letter):
    vowels = "аеио"

    if letter.isalpha():
        if letter in vowels:
            return "Гласна"
        else:
            return "Съгласна"
    else:
        return "Невалидна буква"

# Въвеждане на буква от потребителя
letter = input("Въведете буква: ")

# Проверка на вида на буквата и извеждане на съобщение
result = check_letter_type(letter)
print(f"Буквата '{letter}' е {result}.")
