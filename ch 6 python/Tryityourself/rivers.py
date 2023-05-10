rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'amazon': 'south america',
    }

for river, place in rivers.items():
    print(f"The {river.title()} is in {place.title()}.")

for river in rivers:
    print(river.title())

for place in rivers.values():
    print(place.title())