#Напишете програма, която чете две цели числа, въведени от потребителя и отпечатвапо-голямото от двете.
#● Прочетете две цели числа от конзолата● Сравнете дали първото число е по-голямо от второто.
#Примерен вход и изход


number1 = int(input("Enter first numer:"))
number2 = int(input("Enter second numer:"))

if number1 > number2:
    print(number1)
elif number1 <= number2:
    print(number2)
    
