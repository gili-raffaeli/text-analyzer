import json
from preprocess import Preprocess
from search_engine import SearchEngine
import utils

# python -m pytest

def q4_test(sentences_path, kseq_query_keys_path, remove_words_path, output_path) -> bool:
    try:
        preprocessor = Preprocess(remove_words_path, sentences_path)
        preprocessed_sentences = preprocessor.get_preprocessed_sentences()
        query_data = json.loads(utils.read_json_file_to_str(kseq_query_keys_path))
        search_engine = SearchEngine(preprocessed_sentences, preprocessor.clean_List_List_str(query_data["keys"]))
        search_result = search_engine.to_dict()
        actual_json_str = utils.to_json_str(search_result)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q4_examples/example_1/sentences_small_1.csv',
        "kseq_query_keys_path": 'examples/Q4_examples/example_1//kseq_query_keys_1.json',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q4_examples/example_1/Q4_result1.json',
    }
    assert q4_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q4_examples/example_2/sentences_small_2.csv',
        "kseq_query_keys_path": 'examples/Q4_examples/example_2//kseq_query_keys_2.json',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q4_examples/example_2/Q4_result2.json',
    }
    assert q4_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q4_examples/example_3/sentences_small_3.csv',
        "kseq_query_keys_path": 'examples/Q4_examples/example_3//kseq_query_keys_3.json',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q4_examples/example_3/Q4_result3.json',
    }
    assert q4_test(**input)

def test4():
    input = {
        "sentences_path": 'examples/Q4_examples/example_4/sentences_small_4.csv',
        "kseq_query_keys_path": 'examples/Q4_examples/example_4//kseq_query_keys_4.json',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q4_examples/example_4/Q4_result4.json',
    }
    assert q4_test(**input)
