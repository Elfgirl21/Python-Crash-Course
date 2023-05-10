import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'ch 16 downloading data\data\death_valley_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#get dates, highs, and lows temps from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
#plot high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5) 
#shading b/w highs and lows
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #1-completely opaque

#format plot
ax.set_title("Daily high and low temperatures for Death Valley- 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #draws the date labels diagonally
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()