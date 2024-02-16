#напишете програма, която при въведена година на раждане извежда дали съобщението 
#потребителят е непълнолетен или пълнолетен

import datetime

def check_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year

    if age >= 18:
        return "Пълнолетен"
    else:
        return "Непълнолетен"

# Въвеждане на година на раждане от потребителя
birth_year = int(input("Въведете година на раждане: "))

# Проверка на възрастта и извеждане на съобщение
result = check_age(birth_year)
print(f"Потребителят е {result}.")
