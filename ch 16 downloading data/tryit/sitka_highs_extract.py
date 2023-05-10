import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'ch 16 downloading data\data\sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader)

    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    #getdates and high temps from this file
    dates, highs, lows = [], [], []
    for row in reader:
        if not place_name:
            place_name = row[name_index]
            print(place_name)

        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing for data for {current_date}")
        else:
            dates.append(current_date) 
            highs.append(high)
            lows.append(low)
    
#plot high temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#format plot
ax.set_title("Daily high temperatures for Sitka, Alaska 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #draws the date labels diagonally
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()