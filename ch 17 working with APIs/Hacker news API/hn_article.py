import requests
import json

#make API call, and store the response
url = 'https://hacker-news.fireaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Explore the structure of data
response_dict = r.json()
readable_file = 'ch 17 working with APIs/data/readable_hn_data.json'
with open(readable_file) as f:
    json.dump(response_dict, indent=4)