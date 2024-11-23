import json
import pandas as pd
from sqlalchemy import create_engine

# Load JSON data from Postman response
with open('path/to/your_postman_response.json', 'r') as file:
    json_data = json.load(file)

# Convert JSON to DataFrame
data = pd.json_normalize(json_data)

# Connect to SQL database (replace with your credentials and database details)
engine = create_engine('postgresql://username:password@localhost:5432/your_database')

# Insert data into SQL database table
data.to_sql('your_table_name', engine, if_exists='append', index=False)
