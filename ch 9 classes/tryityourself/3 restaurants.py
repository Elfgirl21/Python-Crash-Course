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
restaurant.describe_restaurant()

rest_0 = Restaurant('Jin', 'Korean')
rest_0.describe_restaurant()

rest_3 = Restaurant('Whataburger', 'American')
rest_3.describe_restaurant()