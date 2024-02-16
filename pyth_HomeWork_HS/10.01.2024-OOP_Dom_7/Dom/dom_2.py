# # 2. Създайте клас с име Mammal.
# При инициализацията, той трябва да получи name, type и sound.
# Създайте клас атрибут наречен kingdom, който не бива да се достъпва извън класа и
# го задайте на “animals”.
# Направете още три метода на инстанцията:
# • make_sound – връща низ във формата "{name} makes {sound}“
# • get_kingdom – връща private атрибут на царство (kingdom)
# • info() – връща низ във формата "{name} is of type {type}"

class Mammal:
    kingdom = "animals"
    
    def __init__(self, name, type, sound):
        self.__name = name
        self.__type = type
        self.__sound = sound
    
    def make_sound(self):
        return f"{self.__name} makes {self.__sound}"
    
    def get_kingdom(self):
        return self.kingdom
    
    def info(self):
        return f"{self.__name} is of type {self.__type}"

mammal = Mammal("Dog", "Domestic", "Bark")

print(mammal.make_sound())
print("Kingdom:", mammal.get_kingdom())
print(mammal.info())
