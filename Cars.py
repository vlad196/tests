#Импортирую класс в код
from modules.Classes import Car

my_car = Car("audi", "a4", 2017)
my_car.update_odometer(23)
my_car.increment_odometer(1)

my_car.read_odometer()