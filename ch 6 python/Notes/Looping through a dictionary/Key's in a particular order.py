favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
#used sorted() function get a copy of keys in order Aa-Z)
for name in sorted(favorite_languages.keys()): #list all keys and sort list before looping through it.
    print(f"{name.title()}, thank you for taking the poll.")