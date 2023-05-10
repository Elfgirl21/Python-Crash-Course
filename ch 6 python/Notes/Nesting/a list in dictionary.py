# sometimes useful put a list in dic
# EX: store info about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza " #python will combine all strings inside of parentheses
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")