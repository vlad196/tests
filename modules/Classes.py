#Изучение классов и экхемпляров
class Car():
    """Class for create a car"""
    def __init__(self, make, model, year):
        """Initialization attributes a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        """Return description of a car"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        """input odometer the car"""
        print("пробег этого авто " + str(self.odometer_reading))
    def update_odometer(self, km):
        """Setup new odometer"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("нет!")
    def increment_odometer(self, km):
        """Increase odometer"""
        if km > 0:
            self.odometer_reading += km
        else:
            print("Неправильный прирост")


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


#Создаю класс пользователя с логированием и разлогирование
class user():
    """Здесь будут атрибуты для логина"""
    def __init__(self, username, password, value):
        self.username = username
        self. password = password
        self.value = value
        print("Добро пожаловать! Пожалуйста авторизуйтесь")

    def login(self, log_username, log_password):
        if log_username == self.username and log_password == self.password:
            self.value +=1
            print("добро пожаловать")
            print("зашёл", self.value, " раз(а)")
        else:
            print("неправильный логин или пароль")