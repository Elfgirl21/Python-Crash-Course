glossary = {
    'string': 'series of characters',
    'integers': 'are real numbers',
    'float': 'decimal point',
    'list' : 'collection of items',
    'dictionary': 'collection of key-vale pairs'
    }

for key, value in glossary.items():
    print(f'\n{key.title()}:')
    print(f"{value}")