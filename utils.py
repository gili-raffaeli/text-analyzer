import json
import os
import tempfile
from typing import Dict, List

def is_processed_sentences_type(variable: any) -> bool:
    if isinstance(variable, list) and all(
        isinstance(inner_list, list) and all(isinstance(item, str) for item in inner_list)
        for inner_list in variable
    ):
        return True
    else:
        return False
    
def is_processed_people_type(variable: any) -> bool:
    if not isinstance(variable, list):
        return False
    for item in variable:
        if not isinstance(item, list) or len(item) != 2:
            return False
        if not isinstance(item[0], list) or not all(isinstance(x, str) for x in item[0]):  # Names list
            return False
        if not isinstance(item[1], list) or not all(isinstance(x, list) and all(isinstance(y, str) for y in x) for x in item[1]):  # Nicknames list
            return False
    return True
    
def turn_Dict_str_any_to_List_any(object: Dict[str, any]) -> List[any]:
    try:
        return [[key, value] for key, value in object.items()]
    except Exception as e:
            print(f"Error in turn_Dict_str_any_to_List_any: {e}")

def to_json_str(object) -> str:
    try:
        return json.dumps(object, indent=4)
    except TypeError as e:
        print(f"Error in to_json_str: {e}")
        return ""
    
def read_json_file_to_str(file_path) -> str:
    try:
        with open(file_path, mode='r') as file:
            expected_output = file.read()
        expected_json = json.loads(expected_output)
        expected_json_str = to_json_str(expected_json)
        return expected_json_str
    except TypeError as e:
        print(f"Error in read_json_file_to_str: {e}")
        return ""
    
def read_json_file(file_path):
    try:
        with open(file_path, mode='r') as file:
            expected_output = file.read()
        return json.loads(expected_output)
    except Exception as e:
        print(f"Error in read_json_file: {e}")
        return None
    
def create_temp_file(content: str, suffix=".csv") -> str:
    """Creates a temporary file with the given content and returns its path."""
    temp = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=suffix)
    try:
        temp.write(content)
        temp.flush() 
        temp.close()
        return temp.name
    except Exception as e:
        temp.close()
        os.unlink(temp.name)
        raise e

