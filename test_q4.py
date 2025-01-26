import json
from count_person_mentions import CountPersonMentions
from preprocess import Preprocess
from k_seq import KSeq
from search_engine import SearchEngine
import utils

# python -m pytest

def q1_check(sentences_path, kseq_query_keys_path, remove_words_path, output_path) -> bool:
    try:
        # print('1')
        people_path = 'examples/Q3_examples/example_4/people_small_4.csv' #
        pre = Preprocess(sentences_path, people_path, remove_words_path)
        pre_sentences = pre.get_sentences()
        num = pre.get_max_main_name_len()
        # print('2')
        x = KSeq(pre_sentences, num).count_q_seq()
        data = json.loads(utils.read_json_file(kseq_query_keys_path))
        xxx = []
        # print('3')
        for seq in data["keys"]:
            if len(seq) == 0: continue
            seqqq = []
            for word in seq:
                if len(word) == 0: continue
                x= pre.clean_text(word)
                y = pre.remove_words(x)
                seqqq.extend(y)
            if seqqq != []: xxx.append(seqqq)
        search = SearchEngine(pre_sentences, xxx).get_format()
        actual_output = json.dumps(search, indent=4)
        actual_json = json.loads(actual_output)
        # print('4')
        actual_json_str = json.dumps(actual_json, indent=4, sort_keys=True)
        # print('5')
        expected_json_str = utils.read_json_file(output_path)
        # print('6')

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
    assert q1_check(**input)

def test2():
    input = {
        "sentences_path": 'examples/Q4_examples/example_2/sentences_small_2.csv',
        "kseq_query_keys_path": 'examples/Q4_examples/example_2//kseq_query_keys_2.json',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q4_examples/example_2/Q4_result2.json',
    }
    assert q1_check(**input)

def test3():
    input = {
        "sentences_path": 'examples/Q4_examples/example_3/sentences_small_3.csv',
        "kseq_query_keys_path": 'examples/Q4_examples/example_3//kseq_query_keys_3.json',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q4_examples/example_3/Q4_result3.json',
    }
    assert q1_check(**input)

def test4():
    input = {
        "sentences_path": 'examples/Q4_examples/example_4/sentences_small_4.csv',
        "kseq_query_keys_path": 'examples/Q4_examples/example_4//kseq_query_keys_4.json',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q4_examples/example_4/Q4_result4.json',
    }
    assert q1_check(**input)

# test1()
# test2()
# test3()
# test4()