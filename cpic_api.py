import requests
import json
import csv



# from extracting_data import extract_data
#
CYP2C19 = {}
# count = 0
# items = extract_data()
# list = []
# for i in range(len(items)):
#     for k,v in items[i].items():
#         list.append(k)
#
# diplotype = 0
# for i in range(len(list)):
#     diplotype = list[i]
#     f_dip = diplotype.split("/")
#     f_dip1 = int(f_dip[1].strip(" *"))
#     if f_dip[0] == "*1" and f_dip[1]== "*2":
#         stop = True
#     full_dip = {"CYP2C9": {f_dip[0]: f_dip1}}
#
#     # Encode the JSON as a URL-encoded string
#     encoded_data = str(full_dip).replace("'", '"')

    # Construct the full URL
url = "https://api.cpicpgx.org/v1/recommendation?select=drug(name), guideline(name), * &drugid=eq.RxNorm:36437&lookupkey=cs.{\"CYP2C19\": \"Ultrarapid Metabolizer\"}"

    #url = f'https://api.cpicpgx.org/v1/rpc/recommendation_lookup?diplotypelookup={encoded_data}'
#url = ['https://api.cpicpgx.org/v1/rpc/recommendation_lookup?diplotypelookup={"CYP2C19": {"*1": 2}}', 'https://api.cpicpgx.org/v1/rpc/recommendation_lookup?diplotypelookup={"CYP2C19": {"*2": 2}}']

payload={}
headers = {}

update = {}

for item in url:
    response = requests.request("GET", item, headers=headers, data=payload)
    data = response.json()
    if not data:
        continue
    else:
        for i in range(len(data)):
            if CYP2C19.get(i) is None:
                update[i] = dict(zip(data[i].keys(), data[i].values()))
            else:
                count = len(CYP2C19)
                update[count + i] = dict(zip(data[i].keys(), data[i].values()))

            CYP2C19.update(update)
            #CYP2C9[i] = {data[i]['drugname'],data[i]["drugrecommendation"],data[i]["phenotypes"],data[i]["guidelineurl"]}
with open('CYP2C19Rec.csv', 'w', newline='') as csvfile:
            #keys = CYP2C9.keys()
    writer = csv.writer(csvfile)
            #writer.writeheader()
    writer.writerows(CYP2C19.items())



