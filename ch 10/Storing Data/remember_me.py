#saving & reading User=generate Data
import json

username = input("What is your name? ")

filename= 'ch 10/Storing Data/username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")