# 5. Създайте клас наречен (Vehicle).
# При инициализация, той трябва да получава max_speed (int - по избор; по
# подразбиране 150) и mileage (number).
# Създайте променлива на инстанцията наречена (gadgets) - празен списък по
# подразбиране.

class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []

# Пример за използване
# Създаване на инстанция с подразбираща се max_speed (150)
vehicle_instance = Vehicle(mileage=10000)

# Извеждане на информация за инстанцията
print(f"Mileage: {vehicle_instance.mileage}")
print(f"Max Speed: {vehicle_instance.max_speed}")
print(f"Gadgets: {vehicle_instance.gadgets}")
