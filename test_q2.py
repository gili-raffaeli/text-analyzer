import json
from preprocess import Preprocess
from k_seq import KSeq

# python -m pytest

def q1_check(sentences_path, people_path, remove_words_path, output_path, n) -> bool:
    try:
        with open(output_path, mode='r') as file:
            expected_output = file.read()

        preprocess_object = Preprocess(sentences_path, people_path, remove_words_path)
        k_seq = KSeq(preprocess_object.get_sentences(), n)
        actual_output = k_seq.to_json()

        expected_json = json.loads(expected_output)
        actual_json = json.loads(actual_output)

        expected_json_str = json.dumps(expected_json, indent=4, sort_keys=True)
        actual_json_str = json.dumps(actual_json, indent=4, sort_keys=True)

        return expected_json_str == actual_json_str
    except:
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q2_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q2_examples/example_1/people_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q2_examples/example_1/Q2_result1.json',
        "n": 3
    }
    assert q1_check(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q2_examples/example_2/sentences_small_2.csv',
        "people_path": 'examples/Q2_examples/example_2/people_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q2_examples/example_2/Q2_result2.json',
        "n": 4
    }
    assert q1_check(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q2_examples/example_3/sentences_small_3.csv',
        "people_path": 'examples/Q2_examples/example_3/people_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q2_examples/example_3/Q2_result3.json',
        "n": 5
    }
    assert q1_check(**input)

