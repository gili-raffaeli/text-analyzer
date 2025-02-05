import json
import os
import tempfile
from pathlib import Path

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
        expected_json_str = to_json_str(expected_json) if expected_json else ""
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

def is_valid_int(var: any) -> bool:
    """Validates if the input variable is a positive integer."""
    if type(var) != int or var < 1: 
        print("invalid input")
        return False
    return True

def is_valid_file(file_path: any) -> bool:
    """Checks if the given file path is a valid existing file."""
    if not isinstance(file_path, str) or not Path(file_path).exists():
        print("invalid input")
        return False
    return True

def validate_args(args) -> bool:
    """Validates command-line arguments before execution."""
    try:
        if args.preprocessed is None:
            if not is_valid_file(args.removewords) or not is_valid_file(args.sentences): return False
            if args.task not in ['2', '4', '9']:
                if not is_valid_file(args.names): return False
        else:
            if not is_valid_file(args.preprocessed): return False

        if args.task == '1':
            if not is_valid_file(args.removewords) or not is_valid_file(args.sentences): return False
        elif args.task == '2':
            if not is_valid_int(args.maxk): return False
        elif args.task == '3': pass
        elif args.task == '4':
            if not is_valid_file(args.qsek_query_path): return False 
        elif args.task == '5':
            if not is_valid_int(args.maxk): return False
        elif args.task in ['6', '7', '8']:
            if not is_valid_int(args.windowsize) or not is_valid_int(args.threshold): return False
            if args.task in ['7', '8']:
                if not is_valid_file(args.pairs): return False
                if args.task == '7':
                    if not is_valid_int(args.maximal_distance): return False
                elif args.task == '8':
                    if not is_valid_int(args.fixed_length): return False
        elif args.task == '9':
            if not is_valid_int(args.threshold): return False 
        else:
            print("invalid input")
            return False
        return True
    except:
        print("invalid input")
        return False

def json_print(object):
    """Prints a Python object as a formatted JSON string."""
    print(to_json_str(object))
