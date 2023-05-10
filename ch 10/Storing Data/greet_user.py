#greet the user
import json

filename = 'ch 10/Storing Data/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")