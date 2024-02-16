# 3. Създайте папка project, в която направете два файла със следните имена:
# • food.py
# • fruit.py
# Във файла food.py, създайте клас наречен Food, който при инициализация ще
# получава дата на изтичане на срока (expiration_date) като низ от символи (str).
# Във файла fruit.py, създайте клас наречен Fruit, който при инициализация ще
# получава име (name) като низ от символи (str) и дата на изтичане на срока
# (expiration_date) също като низ (str).
# Класът Fruit трябва да наследява класа Food.


# Във файла fruit.py
from food import Food

class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name

# Пример за използване в друг файл или интерактивна среда
from food import Food
from fruit import Fruit

food_item = Food("2024-12-31")
fruit_item = Fruit("Apple", "2024-01-21")

print(f"Food item expiration date: {food_item.expiration_date}")
print(f"Fruit item name: {fruit_item.name}")
print(f"Fruit item expiration date: {fruit_item.expiration_date}")
