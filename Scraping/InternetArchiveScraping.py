import requests
import pandas as pd
items = []
initial = "http://archive.org/wayback/available"
# iterate through list of flagged twitter screen names
i = 0

a = pd.read_csv("exhibit_b.csv")

for index, row in a.iterrows():
    par = {"url": "http://twitter.com/" + row["handle"]}
    r = requests.get(initial, params=par)
    items.append(r.json())
# write URL of any available archives to file
with open('./avail_urls.txt', 'w') as f:
    for item in items:
        if 'archived_snapshots' in item:
            if 'closest' in item['archived_snapshots']:
                f.write(item['archived_snapshots']['closest']['url'] + '\n')
