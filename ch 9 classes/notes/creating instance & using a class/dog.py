class Dog:
    """a simple attempt to model a dog."""

    def __init__(self, name, age):
        """initialize name and age attributes."""
        self.name = name
        self.age = age

    
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

#instance representing a specific dog
my_dog = Dog('Willie', 6)
print(f"My name's name is {my_dog.name}.") #dot notation to access attributes of an instance
print(f"My dog is {my_dog.age} years old.")
my_dog.sit() # calling a method instance name(my_dog), dot, method
my_dog.roll_over()
