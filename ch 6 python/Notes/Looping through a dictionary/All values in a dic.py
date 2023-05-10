favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#values() method returns list of values w/out keys
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#check for repetition, used  a set
# set - collection in which eat item must be unique
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #python identifies unique items in list & builds a set from items
    print(language.title())