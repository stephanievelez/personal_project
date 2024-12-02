import json

# Load both JSON files
with open('CYP2C19Rec.json', 'r') as file1:
    first_data = json.load(file1)

with open('CYP2C19', 'r') as file2:
    second_data = json.load(file2)

diplotypekey ={} #second data is a list of dictionaries
lookupkey = []
# Extract `diplotypekey` from second JSON
for i in range(len(second_data)):
    info = second_data[i]
    title = info.get("lookupkey")
    lookupkey.append(title)
    diplotype = info.get("diplotype")
    diplotypekey[i] = info.get("diplotype", {})


# this functions merges lookupkey with their diplotypes
for i, item in enumerate(lookupkey):
    for key, value in item.items():
        # Add the value from diplotypekey to the current dictionary
        if i in diplotypekey:
            item["diplotype"] = diplotypekey[i]
            break


lookupkey

# Create training pairs
training_pairs = []

for drug, entries in first_data.items():
    for entry_id, details in entries.items(): #entries are the values from first_data.items
        phenotypes = details.get("phenotypes", {})
        recommendation = details.get("drugrecommendation", "")

        # Construct prompt using phenotypes
        prompt = f"Given the following information:\n- Phenotypes:\n"
        for gene, phenotype in phenotypes.items():
            #prompt += f"  {gene}: {phenotype}\n"
            if gene != "CYP2C19":
                continue
                #phenotypes.pop(gene)
            items = phenotypes[gene]
            for i in range(len(lookupkey)):
                gene_lookup = lookupkey[i].get('CYP2C19')
                #gene_lookup2 = items['CYP2C19']
                if gene_lookup == items:
                    diplotype_info = lookupkey[i].get("diplotype")
                    prompt += f"- Diplotype:\n  {gene}: {items} : {diplotype_info}\n"
                    break

            # Add related diplotype if available
            # if gene in diplotypekey:
            # if items in lookupkey:
            #     diplotype_str = diplotypekey[gene][1]
            #     diplotype_info = second_data.get("diplotype", f"{gene}: Not Available")
            #     prompt += f"- Diplotype:\n  {gene}: {diplotype_info}\n"

        prompt += f"\nWhat is the drug recommendation for {drug}?"

        # Append to training pairs
        training_pairs.append({"prompt": prompt, "completion": recommendation})
#
# Save training pairs as JSONL
with open('training_data2.jsonl', 'w') as outfile:
    for pair in training_pairs:
        json.dump(pair, outfile)
        outfile.write('\n')

print("Training data prepared successfully!")
