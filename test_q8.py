import json
import timeit
from people_connections import PeopleConnections
from preprocess import Preprocess
import utils

def q8_test(sentences_path, people_path, people_connections, remove_words_path, output_path, window_size, threshold, maximal_distance, fixed_length) -> bool:
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
        start_time = timeit.default_timer()
        result = PeopleConnections(preprocessed_sentences, preprocessed_people, window_size, threshold).task_7_8_format(formated, maximal_distance, fixed_length)
        end_time = timeit.default_timer()
        runtime = end_time - start_time
        # print("runtime: ", runtime)
        actual_json_str = utils.to_json_str(result)
        # print("actual_json_str: ", actual_json_str)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        print('failed')
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q8_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q8_examples/example_1/people_small_1.csv',
        "people_connections": "examples/Q8_examples/example_1/people_connections_1.json",
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q8_examples/example_1/Q8_example_1_w_3_threshold_2_fixed_length_2.json',
        "window_size": 3, 
        "threshold" : 2,
        "fixed_length": 2,
        "maximal_distance": 1000
    }
    assert q8_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q8_examples/exmaple_2/sentences_small_2.csv',
        "people_path": 'examples/Q8_examples/exmaple_2/people_small_2.csv',
        "people_connections": "examples/Q8_examples/exmaple_2/people_connections_2.json",
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q8_examples/exmaple_2/Q8_example_2_w_3_threshold_2_fixed_length_3.json',
        "window_size": 3, 
        "threshold" : 2,
        "fixed_length": 3,
        "maximal_distance": 1000
    }
    assert q8_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q8_examples/exmaple_3/sentences_small_3.csv',
        "people_path": 'examples/Q8_examples/exmaple_3/people_small_3.csv',
        "people_connections": "examples/Q8_examples/exmaple_3/people_connections_3.json",
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q8_examples/exmaple_3/Q8_example_3_w_3_threshold_2_fixed_length_8.json',
        "window_size": 3, 
        "threshold" : 2,
        "fixed_length": 8,
        "maximal_distance": 1000
    }
    assert q8_test(**input)
    