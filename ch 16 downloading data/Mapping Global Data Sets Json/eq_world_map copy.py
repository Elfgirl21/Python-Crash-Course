import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#explore the structure of the data
filename = 'ch 16 downloading data\data\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts)) -158

mags, lons, lats, hover_texts  = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#map the earthquakes
"""data = [Scattergeo(lon=lons, lat=lats)] - old way, not the best"""
#Scattergeo allows overlay scatter plot of geographic data on a map
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
    'size' : [5*mag for mag in mags],
    'color' : mags,
    'colorscale' : 'Viridis', #scale from dark blue to bright yellow
    'reversescale' : True, #use bright yellow for lowest values
    'colorbar' : {'title': 'Magnitude'},
    },
}] #better - structured as key-value pairs in dictionary

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')