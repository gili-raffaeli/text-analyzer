from preprocess import Preprocess
from sentences_connections import SentencesConnections
import utils

def q9_test(sentences_path, remove_words_path, output_path, threshold) -> bool:
    try:
        preprocessor = Preprocess(remove_words_path, sentences_path)
        preprocessed_sentences = preprocessor.get_preprocessed_sentences()
        result = SentencesConnections(preprocessed_sentences, threshold).task_9_format()
        actual_json_str = utils.to_json_str(result)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        print('failed')
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q9_examples/example_1/sentences_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q9_examples/example_1/Q9_result1.json',
        "threshold" : 1,
    }
    assert q9_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q9_examples/exmaple_2/sentences_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q9_examples/exmaple_2/Q9_result2.json',
        "threshold" : 3,
    }
    assert q9_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q9_examples/exmaple_3/sentences_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q9_examples/exmaple_3/Q9_result3.json',
        "threshold" : 6,
    }
    assert q9_test(**input)
