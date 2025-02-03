from find_connections import FindConnections
from preprocess import Preprocess
import utils

# python -m pytest

def q6_test(sentences_path, people_path, remove_words_path, output_path, window_size, threshold) -> bool:
    try:
        preprocessor = Preprocess(remove_words_path, sentences_path, people_path)
        preprocessed_sentences = preprocessor.get_preprocessed_sentences()
        preprocessed_people = preprocessor.get_preprocessed_people()
        result = FindConnections(preprocessed_sentences, preprocessed_people, window_size, threshold).task_6_format()
        actual_json_str = utils.to_json_str(result)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        print('failed')
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q6_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q6_examples/example_1/people_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q6_examples/example_1/Q6_result1_w4_t4.json',
        "window_size": 4, 
        "threshold" : 4,
    }
    assert q6_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q6_examples/exmaple_2/sentences_small_2.csv',
        "people_path": 'examples/Q6_examples/exmaple_2/people_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q6_examples/exmaple_2/Q6_result2_w3_t2.json',
        "window_size": 3, 
        "threshold" : 2,
    }
    assert q6_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q6_examples/exmaple_3/sentences_small_3.csv',
        "people_path": 'examples/Q6_examples/exmaple_3/people_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q6_examples/exmaple_3/Q6_result2_w5_t2.json',
        "window_size": 5, 
        "threshold" : 2,
    }
    assert q6_test(**input)
test3()
def test4():
    input = {
        "sentences_path": 'examples/Q6_examples/exmaple_4/sentences_small_4.csv',
        "people_path": 'examples/Q6_examples/exmaple_4/people_small_4.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q6_examples/exmaple_4/Q6_result2_w5_t1.json',
        "window_size": 5, 
        "threshold" : 1,
    }
    assert q6_test(**input)
