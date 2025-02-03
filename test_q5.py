from person_contexts import PersonContexts
from preprocess import Preprocess
import utils

# python -m pytest

def q5_test(sentences_path, people_path, remove_words_path, output_path, sequence_length) -> bool:
    try:
        preprocessor = Preprocess(remove_words_path, sentences_path, people_path)
        preprocessed_sentences = preprocessor.get_preprocessed_sentences()
        preprocessed_people = preprocessor.get_preprocessed_people()
        result = PersonContexts(preprocessed_sentences, preprocessed_people, sequence_length).task_5_format()
        actual_json_str = utils.to_json_str(result)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        print('failed')
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q5_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q5_examples/example_1/people_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q5_examples/example_1/Q5_result1.json',
        "sequence_length": 3
    }
    assert q5_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q5_examples/example_2/sentences_small_2.csv',
        "people_path": 'examples/Q5_examples/example_2/people_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q5_examples/example_2/Q5_result2.json',
        "sequence_length": 4
    }
    assert q5_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q5_examples/example_3/sentences_small_3.csv',
        "people_path": 'examples/Q5_examples/example_3/people_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q5_examples/example_3/Q5_result3.json',
        "sequence_length": 5
    }
    assert q5_test(**input)

def test4():
    input = {
        "sentences_path": 'examples/Q5_examples/example_4/sentences_small_4.csv',
        "people_path": 'examples/Q5_examples/example_4/people_small_4.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q5_examples/example_4/Q5_result4.json',
        "sequence_length": 6
    }
    assert q5_test(**input)
