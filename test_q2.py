from preprocess import Preprocess
from k_seq import KSeq
import utils

# python -m pytest

def q2_test(sentences_path, remove_words_path, output_path, sequence_length) -> bool:
    try:
        preprocess_object = Preprocess(remove_words_path, sentences_path)
        k_seq = KSeq(preprocess_object.get_preprocessed_sentences(), sequence_length)
        actual_json_str = utils.to_json_str(k_seq.to_dict())
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q2_examples/example_1/sentences_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q2_examples/example_1/Q2_result1.json',
        "sequence_length": 3
    }
    assert q2_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q2_examples/example_2/sentences_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q2_examples/example_2/Q2_result2.json',
        "sequence_length": 4
    }
    assert q2_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q2_examples/example_3/sentences_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q2_examples/example_3/Q2_result3.json',
        "sequence_length": 5
    }
    assert q2_test(**input)
