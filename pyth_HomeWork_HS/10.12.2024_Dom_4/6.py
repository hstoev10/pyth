#Напишете програма, която изчислява сумата на данък върху доход при въведен доход, 
#според следните правила: 1. до 10, 000 лв. - 10% данък; 2. 10,001 - 20, 000 лв. - 15% данък
#над 20, 000 лв. - 20% данък

def calculate_tax(income):
    if income <= 10000:
        tax_rate = 0.10
    elif income <= 20000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

    tax_amount = income * tax_rate
    return tax_amount

# Въвеждане на доход от потребителя
income = float(input("Въведете доход: "))

# Изчисляване на данъка
tax = calculate_tax(income)

# Извеждане на резултата
print(f"Данъкът върху дохода ви е: {tax:.2f} лв.")
