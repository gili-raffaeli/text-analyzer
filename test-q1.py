import pytest
import json
from preprocess import Preprocess

# python -m pytest --version

def normalize_json_string(json_str):
    """Normalize the JSON string by stripping extra spaces and ensuring consistent line breaks."""
    # Normalize line breaks and strip leading/trailing whitespace
    return "\n".join(json_str.splitlines()).strip()

def test_q1():
    # Q1_example_1
    sentences_path = 'examples/Q1_examples/example_1/sentences_small_1.csv'
    people_path = 'examples/Q1_examples/example_1/people_small_1.csv'
    remove_words_path = 'data/REMOVEWORDS.csv'

    output_path = 'examples/Q1_examples/example_1/Q1_result1.json'

    with open(output_path, mode='r') as file:
        expected_output = file.read()

    # Create Preprocess object and get the actual output as a JSON string
    preprocess_object = Preprocess(sentences_path, people_path, remove_words_path)
    actual_output = preprocess_object.to_json()

    # Parse both the expected and actual outputs as JSON
    expected_json = json.loads(expected_output)
    actual_json = json.loads(actual_output)

    # Serialize both JSON objects back to string with consistent formatting
    expected_json_str = json.dumps(expected_json, indent=4, sort_keys=True)
    actual_json_str = json.dumps(actual_json, indent=4, sort_keys=True)

    # Compare the formatted strings
    assert expected_json_str == actual_json_str

def test_q2():
    sentences_path = 'examplesQ1_examples/example_2/sentences_small_2.csv'
    people_path = 'examples/Q1_examples/example_2/people_small_2.csv'
    remove_words_path = 'data/REMOVEWORDS.csv'

    output_path = 'examples/Q1_examples/example_2/Q1_result2.json'

    with open(output_path, mode='r') as file:
        expected_output = file.read()

    # Create Preprocess object and get the actual output as a JSON string
    preprocess_object = Preprocess(sentences_path, people_path, remove_words_path)
    actual_output = preprocess_object.to_json()

    # Parse both the expected and actual outputs as JSON
    expected_json = json.loads(expected_output)
    actual_json = json.loads(actual_output)

    # Serialize both JSON objects back to string with consistent formatting
    expected_json_str = json.dumps(expected_json, indent=4, sort_keys=True)
    actual_json_str = json.dumps(actual_json, indent=4, sort_keys=True)

    # Compare the formatted strings
    assert expected_json_str == actual_json_str

def test_q3():
    sentences_path = 'examples/Q1_examples/example_3/sentences_small_3.csv'
    people_path = 'examples/Q1_examples/example_3/people_small_3.csv'
    remove_words_path = 'data/REMOVEWORDS.csv'

    output_path = 'examples/Q1_examples/example_3/Q1_result3.json'

    with open(output_path, mode='r') as file:
        expected_output = file.read()

    # Create Preprocess object and get the actual output as a JSON string
    preprocess_object = Preprocess(sentences_path, people_path, remove_words_path)
    actual_output = preprocess_object.to_json()

    # Parse both the expected and actual outputs as JSON
    expected_json = json.loads(expected_output)
    actual_json = json.loads(actual_output)

    # Serialize both JSON objects back to string with consistent formatting
    expected_json_str = json.dumps(expected_json, indent=4, sort_keys=True)
    actual_json_str = json.dumps(actual_json, indent=4, sort_keys=True)

    # Compare the formatted strings
    assert expected_json_str == actual_json_str


test_q1()
test_q2()
test_q3()

# # Q1_example_2

# # Q1_example_3

