from typing import Dict, List
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
        for seq in self.__pro_k_seq:
            # print("seq: ", seq)
            sentences_with_seq = self.all_sentences_with_seq(seq)
            # print("sentences_with_seq: ", sentences_with_seq)
            if sentences_with_seq != [[]]: result[" ".join(seq)] = sentences_with_seq
        return dict(sorted(result.items()))

    def to_dict(self) -> Dict[str, Dict[str, any]]:
        """Formats the sequence counts into a specific structure for output."""
        try:
            k_seq = self.preprocess_k_seq_data()
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
        return utils.to_json_str(self.to_dict())

