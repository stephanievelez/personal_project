import json

#get drugid and name
# Opening JSON file
#use the title of the json file to change the name of the dictionary
def extract_druginfo():
    """this tells me the drugid, drugname, for a given gene to plug into the API address, returns a dictionary where the keys are drugid and the values are drugname"""
    drug_gene = {}
    with open("drug_gene") as drugGene_file:
        data = json.load(drugGene_file)
        for i in range(len(data)):
            if data[i]["genesymbol"]=="CYP2C19":
                drug_gene[data[i]["drugid"]]= data[i]["drugname"]
    drugGene_file.close()
    return drug_gene

def extract_data():
    """getting the lookupkey to plug into the API address, reurns a dictionary"""
    CYP2C19 = {}
    with open("CYP2C19") as gene_file:
        data2 = json.load(gene_file)
        for i in range(len(data2)):
            CYP2C19[i]= data2[i]["lookupkey"]
    gene_file.close()
    return CYP2C19


gene_info = extract_druginfo()
cyp_info = extract_data()

print(gene_info, cyp_info)