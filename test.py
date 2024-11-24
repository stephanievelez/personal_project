import requests
import json
import csv
from extracting_data import extract_druginfo, extract_data

#this might have to become a function, will combine all the important data into one csv file

drugid = extract_druginfo()
geneData = extract_data()
druginfo = []
geneinfo = []
for k,v in drugid.items():
    druginfo.append(k)

for k,v in geneData.items():
    if v in geneinfo:
        continue
    else:
        geneinfo.append(v)

geneinfo= geneinfo[:2]
druginfo = druginfo[:2]
# CYP2C19= {drugid["RxNorm:36437"]: geneinfo[0]}
# testdrug =druginfo[7]
# testgene = geneinfo[0]
for i in range(len(geneinfo)):
    for j in range(len(druginfo)):
        CYP2C19 = {drugid[druginfo[j]]: geneinfo[i]}
        testdrug = druginfo[j]
        test= len(geneinfo[i].items())
        if test > 1: #geneinfo is a list of dictionaries
            keys = geneinfo[i]["lookupkey"]
            for i in keys:
                if 'CYP2C19' != i:
                    del keys[i]
                    testgene = keys
                    formatted_lookupkey = json.dumps(testgene)
                break
        else:
            testgene = geneinfo[i]
            formatted_lookupkey = json.dumps(testgene)

    # Encode the JSON as a URL-encoded string
#encoded_data = str(full_dip).replace("'", '"')

#Construct the full URL

        url = f'https://api.cpicpgx.org/v1/recommendation?drugid=eq.{testdrug}&lookupkey=cs.{formatted_lookupkey}'

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        if not data:
            continue
        else:
            for items in range(len(data)):
                CYP2C19[drugid[druginfo[j]]].update(data[items])
            #CYP2C19[drugid[druginfo[j]]].update(data)
            #def write_json(new_data, filename='data.json'):
        with open("CYP2C19Rec.json", 'r+') as file:
                    # First we load existing data into a dict.
            file_data = json.load(file)
                    # Join new_data with file_data inside emp_details
            file_data.update(CYP2C19)
                    # Sets file's current position at offset.
            file.seek(0)
                    # convert back to json.
            json.dump(file_data, file, indent=4)
            # with open("CYP2C19Rec.json", "w") as outfile:
            #     json.dump(CYP2C19, outfile)
            #     json.update(data)