
# 3. Работа с модули и класове:
# Задача: Дефинирайте клас Calculator с методи за
# основни математически операции и създайте
# инстанция на този клас, за да извършите изчисления

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero!"
        return a / b

# Използване на класа Calculator
calculator_instance = Calculator()

result_add = calculator_instance.add(5, 10)
print(f"Събиране: {result_add}")

result_subtract = calculator_instance.subtract(15, 7)
print(f"Изваждане: {result_subtract}")

result_multiply = calculator_instance.multiply(3, 4)
print(f"Умножение: {result_multiply}")

result_divide = calculator_instance.divide(20, 5)
print(f"Деление: {result_divide}")
