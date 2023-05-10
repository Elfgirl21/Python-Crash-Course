favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items(): #languages hold each value or list 
    print(f"{name.title()}'s favorite languages are:")
    for language in languages: #run through each person's favorite languages
        print(f"\t{language.title()}")