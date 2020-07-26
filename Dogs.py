#Классы
class Dog():
    """Пробная модель собаки"""

    def __init__(self, name, age):
        """Инициализируем атрибуты"""
        self.name = name
        self.age = age
        print("Собака создана")

    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + " села")

    def jump(self):
        """Собака будет прыгать по команде"""
        print(self.name.title() + " прыгнула")

my_dog = Dog("Topik", 4)
my_dog_2 = Dog("Nick", 7)

print(my_dog.age)
print(my_dog.name)

my_dog.jump()
my_dog_2.sit()