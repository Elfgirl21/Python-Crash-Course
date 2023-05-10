def city_country(city, country):
    pair = f"{city.title()}, {country.title()}"
    return pair
city_pair = city_country('paris', 'france')
print(city_pair)

city_pair = city_country('washinnton d.c.', 'usa')
print(city_pair)

city_pair = city_country('london', 'england')
print(city_pair)