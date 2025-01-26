from preprocess import Preprocess
import utils

# python -m pytest

def q1_test(sentences_path, people_path, remove_words_path, output_path) -> bool:
    try:
        preprocess_object = Preprocess(remove_words_path, sentences_path, people_path)
        actual_output_str = utils.to_json_str(preprocess_object.to_dict())
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_output_str
    except:
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q1_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q1_examples/example_1/people_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q1_examples/example_1/Q1_result1.json'
    }
    assert q1_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q1_examples/example_2/sentences_small_2.csv',
        "people_path": 'examples/Q1_examples/example_2/people_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q1_examples/example_2/Q1_result2.json'
    }
    assert q1_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q1_examples/example_3/sentences_small_3.csv',
        "people_path": 'examples/Q1_examples/example_3/people_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q1_examples/example_3/Q1_result3.json'
    }
    assert q1_test(**input)
