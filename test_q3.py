import json
from count_person_mentions import CountPersonMentions
from preprocess import Preprocess
from k_seq import KSeq
import utils

# python -m pytest

def q1_check(sentences_path, people_path, remove_words_path, output_path) -> bool:
    try:
        
        preprocess_object = Preprocess(sentences_path, people_path, remove_words_path)
        print(preprocess_object)
        num = preprocess_object.get_max_main_name_len()
        print(num)
        k_seq = KSeq(preprocess_object.get_sentences(), num).count_q_seq()
        print(k_seq)
        people = CountPersonMentions(preprocess_object.get_people(), k_seq)
        actual_output = people.to_json()
        # print(actual_output)

        actual_json = json.loads(actual_output)
        actual_json_str = json.dumps(actual_json, indent=4, sort_keys=True)
        expected_json_str = utils.read_json_file(output_path)

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
    assert q1_check(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q3_examples/example_2/sentences_small_2.csv',
        "people_path": 'examples/Q3_examples/example_2/people_small_2.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q3_examples/example_2/Q3_result2.json',
    }
    assert q1_check(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q3_examples/example_3/sentences_small_3.csv',
        "people_path": 'examples/Q3_examples/example_3/people_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q3_examples/example_3/Q3_result3.json',
    }
    assert q1_check(**input)

def test4():
    input = {
        "sentences_path": 'examples/Q3_examples/example_4/sentences_small_4.csv',
        "people_path": 'examples/Q3_examples/example_4/people_small_4.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q3_examples/example_4/Q3_result4.json',
    }
    assert q1_check(**input)
