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
    
def turn_Dict_str_any_to_List_any(object: Dict[str, any]) -> List[any]:
    return [[key, value] for key, value in object.items()]

def to_json_str(object) -> str:
    try:
        return json.dumps(object, indent=4)
    except TypeError as e:
        print(f"Error serializing object: {e}")
        return ""
    
def read_json_file_to_str(file_path) -> str:
    try:
        with open(file_path, mode='r') as file:
            expected_output = file.read()
        expected_json = json.loads(expected_output)
        expected_json_str = to_json_str(expected_json)
        return expected_json_str
    except TypeError as e:
        print(f"Error serializing object: {e}")
        return ""
