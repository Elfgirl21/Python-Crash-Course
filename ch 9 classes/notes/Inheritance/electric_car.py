class Car:
    """a simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectriCar(Car):
    """Represent aspects of a car, specific to electric"""

    def __init__(self, make, model, year):
        """initialize attributes of the paraent class."""
        super().__init__(make, model, year) #calls method from parent class
        self.battery_size = 75
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectriCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()