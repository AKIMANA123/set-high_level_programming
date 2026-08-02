#!/usr/bin/python3
"""Script to add all arguments to a Python list and save to JSON file"""


import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list from file if it exists
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command line arguments (excluding script name)
my_list.extend(sys.argv[1:])

# Save the updated list to file
save_to_json_file(my_list, filename)
