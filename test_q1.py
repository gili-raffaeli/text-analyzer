import json
from preprocess import Preprocess
import utils

# python -m pytest

def q1_check(sentences_path, people_path, remove_words_path, output_path) -> bool:
    try:
        with open(output_path, mode='r') as file:
            expected_output = file.read()

        preprocess_object = Preprocess(sentences_path, people_path, remove_words_path)
        actual_output =  preprocess_object.to_json()

        actual_json = json.loads(actual_output)
        actual_json_str = json.dumps(actual_json, indent=4, sort_keys=True)
        expected_json_str = utils.read_json_file(output_path)

        return expected_json_str == actual_json_str
    except:
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q1_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q1_examples/example_1/people_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q1_examples/example_1/Q1_result1.json'
    }
    assert q1_check(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q1_examples/example_2/sentences_small_2.csv',
        "people_path": 'examples/Q1_examples/example_2/people_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q1_examples/example_2/Q1_result2.json'
    }
    assert q1_check(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q1_examples/example_3/sentences_small_3.csv',
        "people_path": 'examples/Q1_examples/example_3/people_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q1_examples/example_3/Q1_result3.json'
    }
    assert q1_check(**input)