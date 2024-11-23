import requests
import json
import csv

CYP2C19 = {}
for i in range(len(data)):
    CYP2C19[i] = {data[i]['drugname']: data[i]["drugrecommendation"]}
data_response= json.loads(data)

CYP2C19_data = data['CYP2C19_details']

# now we will open a file for writing
data_file = open('CYP2C19.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in CYP2C19_data:
    if count == 0:
        # Writing headers of CSV file
        header = data.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(data.values())

data_file.close()




