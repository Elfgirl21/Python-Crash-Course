import csv

filename = 'ch 16 downloading data\data\sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader)

    for index, column_header in enumerate(header_row): #enumerate-returns both index of each item and their value
        print(index, column_header)