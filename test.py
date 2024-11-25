import requests
import json
import csv
from extracting_data import extract_druginfo, extract_data

#this might have to become a function, will combine all the important data into one csv file
def CPIC_api():
    """given the drug and gene data, this function will use the CPIC api to get the recommendations for each drug and gene combination, returns a dictionary"""
    drugid = extract_druginfo()
    geneData = extract_data()
    druginfo = []
    geneinfo = []
    CYP2C19 = {}
    data_dict = {}
    count = 0
    for k,v in drugid.items():
        druginfo.append(k)

    for k,v in geneData.items():
        if v in geneinfo:
            continue
        else:
            geneinfo.append(v)

    geneinfo= geneinfo[4:]
    druginfo = druginfo[4:]
# testdrug =druginfo[7]
# testgene = geneinfo[0]
    for i in range(len(geneinfo)):
        for j in range(len(druginfo)):
            #CYP2C19 = {drugid[druginfo[j]]: geneinfo[i]}
            info = geneinfo[i]
            info2 = drugid[druginfo[j]]
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
                if info2 not in data_dict:
                    data_dict[info2] = {index: value for index, value in enumerate(data)}
                else:
                    count = len(data_dict[info2])
                    data_dict2 = {index: value for index, value in enumerate(data, start=count)}
                    data_dict[info2].update(data_dict2)
            # if drugid[druginfo[j]] in CYP2C19:
            #     # Update the existing drug entry
            #     data_dict['gene'] = geneinfo[i]
            #     CYP2C19[drugid[druginfo[j]]].update(data_dict['gene'])
            # else:
            #     # Add a new drug entry
            #     CYP2C19[drugid[druginfo[j]]] = data_dict
    return data_dict

gene = CPIC_api()



