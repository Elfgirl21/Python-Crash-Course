food = 'Korean'
print("Is food == 'Korean'? I predict True.")
print(food == 'Korean')

print("\nIs food == 'Japanese?")
print(food == 'Japanese')
print("\n")

age_0 = 18
age_1 = 20
print(age_1 >= 21) and(age_0 >= 21)
print("\n")

toppings = ['mushrooms', 'onions', 'pineapple']
requested_topping = 'pepperoni'

if requested_topping in toppings:
    print("Yea!")
else:
    print("NO!")

numbers = [0,1,2,3,4,5,6,7,8,9]

for x in numbers:
    if x == 2:
        print('Even number 2')
    else:
        print("Not 2.")
print("\n")

age_3 = 16
age_4 = 64
print( age_3 <= 18 or age_4 <= 18)
print("\n")

name = "Lauren"
print(name.lower() == "lauren")