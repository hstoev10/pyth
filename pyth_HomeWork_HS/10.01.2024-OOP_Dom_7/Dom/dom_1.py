# 1. Създайте клас с име Person. ctrl+shift+U za nov terminal
# При инициализацията, той трябва да получи name и age.
# Скрийте името и възрастта като private атрибути, които не са достъпни извън класа.
# Създайте два метода на инстанцията наречени get_name и get_age, които да връщат
# стойностите на private атрибутите.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

person = Person("Иван", 25)

print("Име:", person.get_name())
print("Възраст:", person.get_age())
