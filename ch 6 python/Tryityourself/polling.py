favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['erin', 'jen', 'sarah', 'edward', 'phil', 'levi', 'eren']

for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take the poll.")