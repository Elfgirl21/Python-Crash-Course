def city_country(city, country, population=''):
    if population:
        pair = f"{city.title()}, {country.title()} - population {population}"
    else:
        pair = f"{city.title()}, {country.title()}"
    return pair
