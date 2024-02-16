# 4. В папка наречена (project) създайте два файла със следните имена:
# • animal.py
# • dog.py
# Във файла animal.py, създайте клас наречен (Animal) с единствен метод eat(), който
# връща: “eating…”
# Във файла dog.py, създайте клас наречен (Dog) с единствен метод bark(), който
# връща: "barking…"
# Класът (Dog) трябва да наследява от класа (Animal).

# Във файла dog.py
from animal import Animal

class Dog(Animal):
    def bark(self):
        return "barking..."

# Пример за използване в друг файл или интерактивна среда
from animal import Animal
from dog import Dog

animal_instance = Animal()
dog_instance = Dog()

print(animal_instance.eat())  # Очакван изход: "eating..."
print(dog_instance.eat())      # Очакван изход: "eating..." (наследен от Animal)
print(dog_instance.bark())     # Очакван изход: "barking..."
