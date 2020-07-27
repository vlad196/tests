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

User1 = user("vlad1.96", "qwerty12", 0)
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())
User1.login(input(), input())