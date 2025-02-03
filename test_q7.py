import json
from find_connections import FindConnections
from preprocess import Preprocess
import utils

# python -m pytest

def q7_test(sentences_path, people_path, people_connections, remove_words_path, output_path, window_size, threshold, maximal_distance) -> bool:
    try:
        preprocessor = Preprocess(remove_words_path, sentences_path, people_path)
        preprocessed_sentences = preprocessor.get_preprocessed_sentences()
        preprocessed_people = preprocessor.get_preprocessed_people()
        try:
            with open(people_connections, mode='r') as file:
                expected_output = file.read()
            expected_json = json.loads(expected_output)
        except:
            print("oops")
        formated = sorted([sorted(name for name in pair) for pair in expected_json["keys"]])
        result = FindConnections(preprocessed_sentences, preprocessed_people, window_size, threshold).task_7_8_format(formated, maximal_distance)
        actual_json_str = utils.to_json_str(result)
        print("actual_json_str: ", actual_json_str)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        print('failed')
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q7_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q7_examples/example_1/people_small_1.csv',
        "people_connections": "examples/Q7_examples/example_1/people_connections_1.json",
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q7_examples/example_1/Q7_result1_w5_t2.json',
        "window_size": 5, 
        "threshold" : 2,
        "maximal_distance": 1000
    }
    assert q7_test(**input)
# test1()
def test2():
    input = {
        "sentences_path": 'examples/Q7_examples/exmaple_2/sentences_small_2.csv',
        "people_path": 'examples/Q7_examples/exmaple_2/people_small_2.csv',
        "people_connections": "examples/Q7_examples/exmaple_2/people_connections_2.json",
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q7_examples/exmaple_2/Q7_result2_w3_t2.json',
        "window_size": 3, 
        "threshold" : 2,
        "maximal_distance": 1000
    }
    assert q7_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q7_examples/exmaple_3/sentences_small_3.csv',
        "people_path": 'examples/Q7_examples/exmaple_3/people_small_3.csv',
        "people_connections": "examples/Q7_examples/exmaple_3/people_connections_3.json",
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q7_examples/exmaple_3/Q7_result3_w5_t1.json',
        "window_size": 5, 
        "threshold" : 2,
        "maximal_distance": 1000
    }
    assert q7_test(**input)

def test4():
    input = {
        "sentences_path": 'examples/Q7_examples/exmaple_4/sentences_small_4.csv',
        "people_path": 'examples/Q7_examples/exmaple_4/people_small_4.csv',
        "people_connections": "examples/Q7_examples/exmaple_4/people_connections_4.json",
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q7_examples/exmaple_4/Q7_result4_w5_t2.json',
        "window_size": 5, 
        "threshold" : 2,
        "maximal_distance": 1000
    }
    assert q7_test(**input)
