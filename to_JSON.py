from test import CPIC_api
import json


result_dict = CPIC_api()
# JSON data:

# python object to be appended

# json_object = json.dumps(result_dict, indent = 4) #this is to start writing the json file
# with open("CYP2C19Rec.json", "w") as outfile:
#     outfile.write(json_object)

with open("CYP2C19Rec.json", 'r+') as file: #this one updates the information
# First we load existing data into a dict.
    file_data = json.load(file)
# Join new_data with file_data inside emp_details
    file_data.update(result_dict)
# Sets file's current position at offset.
    file.seek(0)
# convert back to json.
    json.dump(file_data, file, indent=4)
#y = {"pin":110096}

# parsing JSON string:
# z = json.loads(result_dict)
#
# # appending the data
# #z.update(y)
#
# # the result is a JSON string:
# json.dumps(z, indent=4)




