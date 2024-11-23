import requests
import json
import csv
import urllib.parse
import re


from extracting_data import extract_data

match = {}
count = 0
items = extract_data()
list = []
for i in range(len(items)):
    for k,v in items[i].items():
        list.append(k)

diplotype = 0
for i in range(len(list)):
    diplotype = list[i]
    "2x≥3, 27x2"
    f_dip = diplotype.split("/")
    f_dip1 = int(f_dip[1].strip(" *"))
    if f_dip[0] == "*1" and f_dip[1]== "*2":
        stop = True
    full_dip = {"CYP2D6": {f_dip[0]: f_dip1}}

    # Encode the JSON as a URL-encoded string
    encoded_data = str(full_dip).replace("'", '"')

    #Construct the full URL
    url = f'https://api.cpicpgx.org/v1/rpc/recommendation_lookup?diplotypelookup={encoded_data}'

    payload={}
    headers = {}

    update = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    if not data:
        continue
    else:
        count +=1
        match[count] = url
print(match)

