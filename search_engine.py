import json
from typing import Dict, List
from k_seq import KSeq
from preprocess import Preprocess
import utils


class SearchEngine:
    def __init__(self, preprocessed_sentences: List[List[str]], pro_query_keys: List[List[str]]):
        self.__pro_k_seq = pro_query_keys # check
        self.__preprocessed_sentences = preprocessed_sentences # check


    def sentence_with_seq(self, seq: List[str], sentence: List[str]) -> List[str]:
        if len(sentence) < len(seq): return None
        for i in range(len(sentence) - len(seq) + 1):
            if seq == sentence[i:i+len(seq)]:
                return sentence
        return None
    
    def all_sentences_with_seq(self, seq: List[str]) -> List[List[str]]:
        all_sentences = []
        for sentence in self.__preprocessed_sentences:
            is_sentence = self.sentence_with_seq(seq, sentence)
            if is_sentence: all_sentences.append(is_sentence) 
        if all_sentences == []: return [[]]
        return sorted(all_sentences)

    def preprocess_k_seq_data(self) -> Dict[str, List[List[str]]]:
        result = {}
        # print("self.__pro_k_seq: ", self.__pro_k_seq)
        for seq in self.__pro_k_seq:
            # print('seq: ', seq)
            sentences_with_seq = self.all_sentences_with_seq(seq)
            # print("sentences_with_seq: ", sentences_with_seq)
            if sentences_with_seq != [[]]: result[" ".join(seq)] = sentences_with_seq
        return dict(sorted(result.items()))

    def get_format(self):
        """Formats the sequence counts into a specific structure for output."""
        try:
            k_seq = self.preprocess_k_seq_data()
            # print('k_seq: ', k_seq)
            n_seq_list = [[key, value] for key, value in k_seq.items()]

            return {
                "Question 4": {
                    "K-Seq Matches": n_seq_list,
                }
            }
        except Exception as e:
            print("Error: ", e)
            return None
        
    def __str__(self):
        """Returns the string representation of the formatted sequence counts."""
        return str(utils.to_json(self.get_format()))

    
sentences_path = "examples/Q4_examples/example_4/sentences_small_4.csv"
REMOVEWORDS_path = "data/REMOVEWORDS.csv"
Q4_result1_path = "examples/Q4_examples/example_4/Q4_result4.json"
people_path = 'examples/Q3_examples/example_4/people_small_4.csv' #
pre = Preprocess(sentences_path, people_path, REMOVEWORDS_path)
pre_sentences = pre.get_sentences()
num = pre.get_max_main_name_len()
x = KSeq(pre_sentences, num).count_q_seq()
kseq_query_keys_path = "examples/Q4_examples/example_4/kseq_query_keys_4.json"
data = json.loads(utils.read_json_file(kseq_query_keys_path))
# print('data["keys"]: ', data["keys"])
xxx = []
for seq in data["keys"]:
    if len(seq) == 0: continue
    # print("seq: ", seq)
    seqqq = []
    for word in seq:
        if len(word) == 0: continue
        # print("word: ", word)
        x= pre.clean_text(word)
        y = pre.remove_words(x)
        if len(y) == 0: continue
        seqqq.extend(y)
    if seqqq != []: xxx.append(seqqq)
print("xxx: ", xxx)
search = SearchEngine(pre_sentences, xxx).get_format()
print("1: ", search)