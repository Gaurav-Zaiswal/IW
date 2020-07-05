# Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json

my_info_dict = {
    'name': 'Gaurav Jaiswal',
    'age': 22
}

my_info_json = json.dumps(my_info_dict)

print('My info in a Dictionary: {}'.format(my_info_dict))
print('My info in JSON format(from dict to json): {}'.format(my_info_json))
print('My info in a Dictionary(from JSON to dict): {}'.format(json.loads(my_info_json)))
