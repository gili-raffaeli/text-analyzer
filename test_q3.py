from count_person_mentions import CountPersonMentions
from preprocess import Preprocess
from k_seq import KSeq
import utils

# python -m pytest

def q3_test(sentences_path, people_path, remove_words_path, output_path) -> bool:
    try:
        preprocess_object = Preprocess(remove_words_path, sentences_path, people_path)
        longest_name = preprocess_object.get_longest_main_name_len()
        k_seq = KSeq(preprocess_object.get_preprocessed_sentences(), longest_name).count_sequences_len_k()
        people = CountPersonMentions(preprocess_object.get_preprocessed_people(), k_seq).to_dict()
        actual_json_str = utils.to_json_str(people)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        return False

def test1():
    input = {
        "sentences_path": 'examples/Q3_examples/example_1/sentences_small_1.csv',
        "people_path": 'examples/Q3_examples/example_1/people_small_1.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q3_examples/example_1/Q3_result1.json',
    }
    assert q3_test(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q3_examples/example_2/sentences_small_2.csv',
        "people_path": 'examples/Q3_examples/example_2/people_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q3_examples/example_2/Q3_result2.json',
    }
    assert q3_test(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q3_examples/example_3/sentences_small_3.csv',
        "people_path": 'examples/Q3_examples/example_3/people_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q3_examples/example_3/Q3_result3.json',
    }
    assert q3_test(**input)

def test4():
    input = {
        "sentences_path": 'examples/Q3_examples/example_4/sentences_small_4.csv',
        "people_path": 'examples/Q3_examples/example_4/people_small_4.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q3_examples/example_4/Q3_result4.json',
    }
    assert q3_test(**input)
