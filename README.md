CPIC API Data Extraction and Recommendation System
This repository contains Python scripts for interacting with the CPIC database to extract drug recommendations based on genetic information. The extracted data is processed to create JSON files suitable for training large language models (LLMs).

Overview
cpic_api.py
Automates searches through the CPIC database to retrieve drug information linked to specific genes.

Key functionalities:
Extract_data.py:
drug_info function: Extracts drug data, including drugid and drugname, to construct API URLs for further database queries.
extract_data function: Retrieves the lookup key for the gene in question.

testing.py:
Uses the extracted drugid and gene/diplotype information (e.g., {"CYP2C19": {"*1": 2}}) to search for each drug recommendation according to patient's phenotype.
Aggregates recommendations for each drug into a Python dictionary for further processing.

test2.py:
Combines the JSON output from reconciled drug recommendations (based on the gene/diplotype) with gene data.
Produces a prompt-ready JSON file containing drug recommendations, which can be used to train LLMs.
