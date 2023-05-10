import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'ch 16 downloading data\data\sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader)

    #getdates and high temps from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        dates.append(current_date)
        highs.append(high)
    
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