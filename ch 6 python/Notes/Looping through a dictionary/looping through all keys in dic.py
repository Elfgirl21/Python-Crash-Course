favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# keys() method is useful when don't need to work with all values in dictionary
for name in favorite_languages.keys():
    print(name.title())
#same ouput if used
"""
for name in favorite_languages:
looping through keys is default when looping through dictoionaries.
"""
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")