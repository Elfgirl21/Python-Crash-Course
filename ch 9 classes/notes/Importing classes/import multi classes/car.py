"""A class that can be used to represent gas and electric cars."""

class Car:
    """a simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """set odometer reading to the given value
        reject change if it attmepts to roll odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

class Battery:
    """simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75): 
        """initialize the batter's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectriCar(Car):
    """Represent aspects of a car, specific to electric"""

    def __init__(self, make, model, year):
        """initialize attributes of the paraent class."""
        super().__init__(make, model, year) 
        self.battery = Battery()