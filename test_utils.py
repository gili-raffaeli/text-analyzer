import json
import os
from tempfile import NamedTemporaryFile
from utils import (
    to_json_str,
    read_json_file,
    read_json_file_to_str,
    create_temp_file,
    is_valid_int,
    is_valid_file,
    json_print
)

# Test `to_json_str`
def test_to_json_str_valid():
    data = {"name": "Alice", "age": 30}
    expected = json.dumps(data, indent=4)
    assert to_json_str(data) == expected

def test_to_json_str_invalid():
    assert to_json_str(str()) == '""'

# Test `read_json_file`
def test_read_json_file_valid():
    temp = NamedTemporaryFile(delete=False, mode='w', suffix=".json")
    temp.write(json.dumps({"key": "value"}))
    temp.close()
    assert read_json_file(temp.name) == {"key": "value"}
    os.unlink(temp.name)

def test_read_json_file_invalid():
    assert read_json_file("nonexistent.json") is None

# Test `read_json_file_to_str`
def test_read_json_file_to_str_valid():
    temp = NamedTemporaryFile(delete=False, mode='w', suffix=".json")
    data = {"key": "value"}
    temp.write(json.dumps(data))
    temp.close()
    expected = json.dumps(data, indent=4)
    assert read_json_file_to_str(temp.name) == expected
    os.unlink(temp.name)

def test_read_json_file_to_str_invalid():
    assert read_json_file_to_str("nonexistent.json") == ""

# Test `create_temp_file`
def test_create_temp_file():
    content = "hello,world"
    temp_file = create_temp_file(content)
    with open(temp_file, "r") as file:
        assert file.read() == content
    os.unlink(temp_file)

# Test `is_valid_int`
def test_is_valid_int():
    assert is_valid_int(5) == True
    assert is_valid_int(1) == True
    assert is_valid_int(0) == False
    assert is_valid_int(-1) == False
    assert is_valid_int("10") == False
    assert is_valid_int(None) == False

# Test `is_valid_file`
def test_is_valid_file_existing():
    temp = NamedTemporaryFile(delete=False)
    temp.close()
    assert is_valid_file(temp.name) is True
    os.unlink(temp.name)

def test_is_valid_file_non_existing():
    assert is_valid_file("nonexistent_file.txt") is False

def test_is_valid_file_invalid_type():
    assert is_valid_file(123) is False
    assert is_valid_file(None) is False

def test_json_print(capsys):
    data = {"hello": "world"}
    json_print(data)
    captured = capsys.readouterr()
    assert json.loads(captured.out.strip()) == data
