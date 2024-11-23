import json

# Opening JSON file
#use the title of the json file to change the name of the dictionary
def drug_gene():
    '''Extracts data from a json file gene-drug_pair and returns a dictionary of certain items from the data'''
    drug_gene = {}
    with open("drug_gene") as json_file:
        data = json.load(json_file)

    # Print the data of dictionary
        for i in range(len(data)):
            drug_gene[i] = {data[i]['drugid']:data[i]["genesymbol"]}

# Closing file
    json_file.close()
    return drug_gene

print(drug_gene())