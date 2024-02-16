# 3. Създайте папка project, в която направете два файла със следните имена:
# • food.py
# • fruit.py
# Във файла food.py, създайте клас наречен Food, който при инициализация ще
# получава дата на изтичане на срока (expiration_date) като низ от символи (str).
# Във файла fruit.py, създайте клас наречен Fruit, който при инициализация ще
# получава име (name) като низ от символи (str) и дата на изтичане на срока
# (expiration_date) също като низ (str).
# Класът Fruit трябва да наследява класа Food.


# Във файла food.py

class Food:
    def __init__(self, expiration_date):
        self.expiration_date = expiration_date
