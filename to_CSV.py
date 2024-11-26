import csv

from test import CPIC_api
import json
import pandas as pd

# Load the JSON data
with open("CYP2C19Rec.json", "r") as f:
    data = json.load(f)

# Flatten the JSON data
rows = []
for drug, details in data.items():
    for entry in details.values():
        rows.append({
            "drug": drug,
            "CYP2D6": entry["phenotypes"].get("CYP2D6", ""),
            "CYP2C19": entry["phenotypes"].get("CYP2C19", ""),
            "recommendation": entry["drugrecommendation"]
        })

# Create a DataFrame
df = pd.DataFrame(rows)
print(df.head())

# Save to CSV for easier handling
df.to_csv("CYP2C9Rec.csv", index=False)
