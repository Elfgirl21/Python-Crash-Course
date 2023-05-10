cities = {
    'euless' : {
        'country': 'usa',
        'population': 10000,
        'fun fact': 'small',
    },

    'paris': {
        'country' : 'france',
        'population': 10000000,
        'fun fact': 'big'
    },

    'london': {
        'country': 'uk',
        'population': 100000,
        'fun fact': 'rainy'
    },
    
}

for city, city_info in cities.items():
    print(f"{city.title()} info: {city_info['country'].title()}, {city_info['population']}, {city_info['fun fact']}")