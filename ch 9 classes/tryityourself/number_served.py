class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The resutaurant name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def num_served(self):
        print(f"{self.restaurant_name} has served {self.number_served}.")
    
    def increment_number_served(self, served):
        self.number_served += served

restaurant = Restaurant('Jin', 'Korean')
restaurant.number_served = 26
restaurant.increment_number_served(50)
restaurant.num_served()