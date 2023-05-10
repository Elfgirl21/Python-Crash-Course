#json.load() 
import json

filename = 'ch 10/Storing Data/numbers.json' 
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
