import json

# Load both JSON files
with open('CYP2C19Rec.json', 'r') as file1:
    first_data = json.load(file1)

with open('CYP2C19', 'r') as file2:
    second_data = json.load(file2)

diplotypekey ={} #diplotypekey is a list of dictionaries
# Extract `diplotypekey` from second JSON
for i in range(len(second_data)):
    info = second_data[i]
    diplotypekey[i] = second_data[i].get("diplotypekey", {})


# Create training pairs
training_pairs = []

for drug, entries in first_data.items():
    for entry_id, details in entries.items(): #entries are the values from first_data.items(0
        phenotypes = details.get("phenotypes", {})
        recommendation = details.get("drugrecommendation", "")

        # Construct prompt using phenotypes
        prompt = f"Given the following information:\n- Phenotypes:\n"
        for gene, phenotype in phenotypes.items():
            prompt += f"  {gene}: {phenotype}\n"

            # Add related diplotype if available
            if gene in diplotypekey:
                diplotype_info = second_data.get("diplotype", f"{gene}: Not Available")
                prompt += f"- Diplotype:\n  {gene}: {diplotype_info}\n"

        prompt += f"\nWhat is the drug recommendation for {drug}?"

        # Append to training pairs
        training_pairs.append({"prompt": prompt, "completion": recommendation})

# Save training pairs as JSONL
with open('training_data.jsonl', 'w') as outfile:
    for pair in training_pairs:
        json.dump(pair, outfile)
        outfile.write('\n')

print("Training data prepared successfully!")
