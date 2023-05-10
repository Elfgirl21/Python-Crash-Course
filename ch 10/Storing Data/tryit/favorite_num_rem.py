import json

filename = 'ch 10/Storing Data/tryit/favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f"Your favorite number is {number}.")
else:
    print(f"I know your favorite number, it's {number}")
    