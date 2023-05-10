class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The resutaurant name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant('Mate', 'British')
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()