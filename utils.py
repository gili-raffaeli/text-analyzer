import json
import os
import tempfile
from typing import Dict, List

def to_json_str(object) -> str:
    """Converts a Python object to a formatted JSON string."""
    try:
        return json.dumps(object, indent=4)
    except TypeError as e:
        print(f"Error in to_json_str: {e}")
        return ""
    
def read_json_file(file_path):
    """Reads a JSON file and returns its content as a Python object."""
    try:
        with open(file_path, mode='r') as file:
            expected_output = file.read()
        return json.loads(expected_output)
    except Exception as e:
        print(f"Error in read_json_file: {e}")
        return None
    
def read_json_file_to_str(file_path) -> str:
    """Reads a JSON file and returns its content as a formatted JSON string."""
    try:
        expected_json = read_json_file(file_path)
        expected_json_str = to_json_str(expected_json)
        return expected_json_str
    except TypeError as e:
        print(f"Error in read_json_file_to_str: {e}")
        return ""
    
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
