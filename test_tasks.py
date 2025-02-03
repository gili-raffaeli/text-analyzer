import json
from count_people_mentions import CountPeopleMentions
from search_engine import SearchEngine
import utils
from preprocess import Preprocess
from count_words_seq import CountWordsSeq

def task1_test(sentences_path, people_path, remove_words_path, output_path) -> bool:
    try:
        preprocess_object = Preprocess(remove_words_path, sentences_path, people_path)
        actual_output_str = utils.to_json_str(preprocess_object.task_1_format())
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_output_str
    except:
        return False

def task2_test(sentences_path, remove_words_path, output_path, sequence_length) -> bool:
    try:
        preprocess_object = Preprocess(remove_words_path, sentences_path)
        k_seq = CountWordsSeq(preprocess_object.get_preprocessed_sentences(), sequence_length)
        actual_json_str = utils.to_json_str(k_seq.task_2_format())
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        return False

def task3_test(sentences_path, people_path, remove_words_path, output_path) -> bool:
    try:
        preprocess_object = Preprocess(remove_words_path, sentences_path, people_path)
        people = CountPeopleMentions(preprocess_object.get_preprocessed_people(), preprocess_object.get_preprocessed_sentences()).task_3_format()
        actual_json_str = utils.to_json_str(people)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        return False
    
def task4_test(sentences_path, kseq_query_keys_path, remove_words_path, output_path) -> bool:
    try:
        preprocessor = Preprocess(remove_words_path, sentences_path)
        preprocessed_sentences = preprocessor.get_preprocessed_sentences()
        query_data = json.loads(utils.read_json_file_to_str(kseq_query_keys_path))
        search_engine = SearchEngine(preprocessed_sentences, preprocessor.clean_List_List_str(query_data["keys"]))
        search_result = search_engine.task_4_format()
        actual_json_str = utils.to_json_str(search_result)
        expected_json_str = utils.read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        return False

### tests ###

def test_task1():
    inputs = [
        {
            "sentences_path": 'examples/Q1_examples/example_1/sentences_small_1.csv',
            "people_path": 'examples/Q1_examples/example_1/people_small_1.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q1_examples/example_1/Q1_result1.json'
        },
        {
            "sentences_path": 'examples/Q1_examples/example_2/sentences_small_2.csv',
            "people_path": 'examples/Q1_examples/example_2/people_small_2.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q1_examples/example_2/Q1_result2.json'
        },
        {
            "sentences_path": 'examples/Q1_examples/example_3/sentences_small_3.csv',
            "people_path": 'examples/Q1_examples/example_3/people_small_3.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q1_examples/example_3/Q1_result3.json'
        }
    ]
    for input in inputs:
        assert task1_test(**input)

def test_task2():
    inputs = [
        {
            "sentences_path": 'examples/Q2_examples/example_1/sentences_small_1.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q2_examples/example_1/Q2_result1.json',
            "sequence_length": 3
        },
        {
            "sentences_path": 'examples/Q2_examples/example_2/sentences_small_2.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q2_examples/example_2/Q2_result2.json',
            "sequence_length": 4
        },
        {
        "sentences_path": 'examples/Q2_examples/example_3/sentences_small_3.csv',
        "remove_words_path": 'data/REMOVEWORDS.csv',
        "output_path": 'examples/Q2_examples/example_3/Q2_result3.json',
        "sequence_length": 5
    }
    ]
    for input in inputs:
        assert task2_test(**input)

def test_task3():
    inputs = [
        {
            "sentences_path": 'examples/Q3_examples/example_1/sentences_small_1.csv',
            "people_path": 'examples/Q3_examples/example_1/people_small_1.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q3_examples/example_1/Q3_result1.json',
        },
        {
            "sentences_path": 'examples/Q3_examples/example_2/sentences_small_2.csv',
            "people_path": 'examples/Q3_examples/example_2/people_small_2.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q3_examples/example_2/Q3_result2.json',
        },
            {
            "sentences_path": 'examples/Q3_examples/example_3/sentences_small_3.csv',
            "people_path": 'examples/Q3_examples/example_3/people_small_3.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q3_examples/example_3/Q3_result3.json',
        },
        {
            "sentences_path": 'examples/Q3_examples/example_4/sentences_small_4.csv',
            "people_path": 'examples/Q3_examples/example_4/people_small_4.csv',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q3_examples/example_4/Q3_result4.json',
        }
    ]
    for input in inputs:
        assert task3_test(**input)

def test_task4():
    inputs = [
        {
            "sentences_path": 'examples/Q4_examples/example_1/sentences_small_1.csv',
            "kseq_query_keys_path": 'examples/Q4_examples/example_1//kseq_query_keys_1.json',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q4_examples/example_1/Q4_result1.json',
        },
            {
            "sentences_path": 'examples/Q4_examples/example_2/sentences_small_2.csv',
            "kseq_query_keys_path": 'examples/Q4_examples/example_2//kseq_query_keys_2.json',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q4_examples/example_2/Q4_result2.json',
        },
                {
            "sentences_path": 'examples/Q4_examples/example_3/sentences_small_3.csv',
            "kseq_query_keys_path": 'examples/Q4_examples/example_3//kseq_query_keys_3.json',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q4_examples/example_3/Q4_result3.json',
        },
            {
            "sentences_path": 'examples/Q4_examples/example_4/sentences_small_4.csv',
            "kseq_query_keys_path": 'examples/Q4_examples/example_4//kseq_query_keys_4.json',
            "remove_words_path": 'data/REMOVEWORDS.csv',
            "output_path": 'examples/Q4_examples/example_4/Q4_result4.json',
        }
    ]
    for input in inputs:
        assert task4_test(**input)


