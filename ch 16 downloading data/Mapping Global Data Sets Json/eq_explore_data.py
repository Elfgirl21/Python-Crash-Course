import json

#explore the structure of the data
filename = 'ch 16 downloading data\data\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'ch 16 downloading data/data/readable_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)