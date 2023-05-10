import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'ch 16 downloading data\data\sitka_weather_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader)

    #get dates, highs, and lows temps from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
#plot high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) #alpha - controls color's transparency
ax.plot(dates, lows, c='blue', alpha=0.5) #0-completely transparent
#shading b/w highs and lows
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #1-completely opaque

#format plot
ax.set_title("Daily high and low temperatures for Sitka - 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #draws the date labels diagonally
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()