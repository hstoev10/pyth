# 6. Създайте клас наречен (Circle).
# При инициализация, той трябва да получава radius (number). Създайте клас атрибут
# наречен пи (pi), който трябва да бъде равен на 3.14. Създайте 3 метода на
# инстанцията:
# • set_radius (new_radius) – променя радиуса
# • get_area() – връща прощта на кръга
# • get_circumference() – връща обиколката на кръга

class Circle:
    # Клас атрибут
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # Метод за промяна на радиуса
    def set_radius(self, new_radius):
        self.radius = new_radius

    # Метод за изчисление на площта на кръга
    def get_area(self):
        return self.pi * (self.radius ** 2)

    # Метод за изчисление на обиколката на кръга
    def get_circumference(self):
        return 2 * self.pi * self.radius

# Пример за използване
# Създаване на инстанция с radius = 10
circle_instance = Circle(radius=10)

# Извеждане на информация за инстанцията
print(f"Radius: {circle_instance.radius}")
print(f"Area: {circle_instance.get_area()}")
print(f"Circumference: {circle_instance.get_circumference()}")

# Промяна на радиуса и повторно изчисление на площта и обиколката
circle_instance.set_radius(12)
print(f"New Radius: {circle_instance.radius}")
print(f"New Area: {circle_instance.get_area()}")
print(f"New Circumference: {circle_instance.get_circumference()}")
