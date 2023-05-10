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

    def fill_gas_tank(self):
        if self.tank == 0:
            print("Tank empty")
        elif self.tank <= 5:
            print("tank half full")
        else:
            print("tank full")

class Battery:
    """simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75): #battery_size is opitional parameter that can be set if no value is provided
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
        super().__init__(make, model, year) #calls method from parent class
        self.battery = Battery() #add self.battery att
                                 #create new instance of Battery & assigns it to self.battery
    

my_tesla = ElectriCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() #find battery att, call method that associated with Battery instance stored in
                                    #in the att
my_tesla.battery.get_range()