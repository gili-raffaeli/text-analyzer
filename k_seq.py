import json
from typing import Dict, List
import preprocess

class KSeq:
    def __init__(self, preprocessed_sentences, n):
        self.__preprocessed_sentences = preprocessed_sentences #check?
        self.__n = n # check?

    def count_words_in_sentence(self, words: List[str], sentence: List[str]) -> int:
        if len(sentence) < len(words): return 0
        words_count = 0
        for i in range(len(sentence) - len(words) + 1):
            if words == sentence[i:i+len(words)]:
                words_count += 1
        return words_count

    def cont_words(self, words: List[str]) -> int:
        words_count = 0
        for sentence in self.__preprocessed_sentences:
            words_count += self.count_words_in_sentence(words, sentence)
        return words_count
    
    def get_words_len_n(self, n: int) -> List[List[str]]:
        words_len_n = []
        for sentence in self.__preprocessed_sentences:
            if len(sentence) < n: continue
            for i in range(len(sentence) - n + 1):
                if sentence[i:i+n] not in words_len_n:
                    words_len_n.append(sentence[i:i+n])
        return words_len_n

    def n_seq(self, k) -> List[List[any]]:
        n_seq = []
        words_len_n = self.get_words_len_n(k)
        for word_len_n in words_len_n:
            words_cont = self.cont_words(word_len_n)
            n_seq.append([" ".join(word_len_n), words_cont])
        return sorted(n_seq, key=lambda x: x[0])
    
    def count_q_seq(self) -> List[List[List[any]]]:
        k_seq = []
        for k in range(1, self.__n + 1):
            k_seq.append([f"{k}_seq", self.n_seq(k)])
        return k_seq
    
    def get_q_seq(self) -> Dict:
        return {
            "Question 2": {
                f"{self.__n}-Seq Counts": self.count_q_seq()
            }
        }

    def to_json(self) -> str:
        return json.dumps(self.get_q_seq(), indent=4)
    
    def __str__(self):
        return str(self.to_json())


input = {
    "sentences_file": 'examples/Q2_examples/example_1/sentences_small_1.csv',
    "people_file": 'examples/Q2_examples/example_1/people_small_1.csv',
    "remove_words_file": 'data/REMOVEWORDS.csv',
}

# pre = preprocess.Preprocess(**input)
# x = KSeq(pre.get_sentences(), 3)
# q_seq = x.get_q_seq()
# print(q_seq["Question 2"]["3-Seq Counts"])