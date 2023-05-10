favorite_places = {
    'jen' : ['paris', 'london', 'nice'],
    'ben' : ['seattle'],
    'mark': ['la', 'euless'],
}

for name, places in favorite_places.items():
    if len(places) <= 1:
        print(f"{name.title()}'s favorite place is:")
    else:
        print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")