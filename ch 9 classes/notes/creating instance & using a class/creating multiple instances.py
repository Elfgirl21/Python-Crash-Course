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


my_dog = Dog('Willie', 6) # separate instance
your_dog = Dog('Lucy', 3) # spearate instance

print(f"My name's name is {my_dog.name}.") #dot notation to access attributes of an instance
print(f"My dog is {my_dog.age} years old.")
my_dog.sit() # calling a method instance name(my_dog), dot, method

print(f"\nYour dong's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years ago.")
your_dog.sit()
