class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0 #setting default value to this attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

    def readOdometer(self):
        print(self.odometerReading)

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.readOdometer()

my_new_car.odometerReading = 23 #modifying attribute's value
my_new_car.readOdometer()

 class ElectricCar(Car):
     """Represent aspects of a car, specific to electric vehicles."""


    def __init__(self, make, model, year):
         """Initialize attributes of the parent class."""
    super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
