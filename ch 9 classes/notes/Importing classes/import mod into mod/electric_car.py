"""a set of classes that can be used to represent electric cars."""

from car import Car

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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric"""

    def __init__(self, make, model, year):
        """initialize attributes of the paraent class."""
        super().__init__(make, model, year) 
        self.battery = Battery()