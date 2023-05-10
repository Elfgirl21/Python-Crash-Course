import json

number = input("What's your favorite number? ")

filename = 'ch 10/Storing Data/tryit/favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
    print(f"I know your favorite number. It's {number}.")