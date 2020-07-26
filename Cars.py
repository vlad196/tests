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

my_car = Car("audi", "a4", 2017)
my_car.update_odometer(23)
my_car.increment_odometer(1)

my_car.read_odometer()