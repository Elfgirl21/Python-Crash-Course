import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#explore the structure of the data
filename = 'ch 16 downloading data\data\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts)) -158

mags, lons, lats  = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#map the earthquakes
"""data = [Scattergeo(lon=lons, lat=lats)] - old way, not the best"""
#Scattergeo allows overlay scatter plot of geographic data on a map
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {
    'size' : [5*mag for mag in mags],
    },
}] #better - structured as key-value pairs in dictionary

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')