import json
from typing import Any, Dict, List

def is_type_List_List_str(variable: any) -> bool:
    if isinstance(variable, list) and all(
        isinstance(inner_list, list) and all(isinstance(item, str) for item in inner_list)
        for inner_list in variable
    ):
        return True
    else:
        return False
    
def to_json(object) -> str:
    return json.dumps(object, indent=4)

def read_json_file(file_path):
    with open(file_path, mode='r') as file:
        expected_output = file.read()
    expected_json = json.loads(expected_output)
    expected_json_str = json.dumps(expected_json, indent=4, sort_keys=True)
    return expected_json_str