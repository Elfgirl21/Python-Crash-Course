#json.dump() - 2 args: piece of data to store & file object to store the data

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'ch 10/Storing Data/numbers.json' #data store in file in JSON format
with open(filename, 'w') as f:
    json.dump(numbers, f)
