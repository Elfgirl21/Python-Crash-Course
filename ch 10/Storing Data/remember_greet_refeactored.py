import json

def get_stored_username():
    """Get stored username if available."""
    filename= 'ch 10/Storing Data/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None #good practice: function should either return vale expecting or return None
    else:
        return username

def greet_user():
    """Greetthe user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'ch 10/StoringData/username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")

greet_user()