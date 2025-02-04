from typing import Dict, List


class SearchEngine:
    def __init__(self, preprocessed_sentences: List[List[str]], pro_query_keys: List[List[str]]):
        self.__pro_k_seq = pro_query_keys # check
        self.__preprocessed_sentences = preprocessed_sentences # check

    def __is_seq_in_sentence_(self, seq: List[str], sentence: List[str]) -> bool:
        """Checks if a given sequence appears in a sentence."""
        if len(sentence) < len(seq): return False
        seq_str = " ".join(seq)
        sentence_str = " ".join(sentence)
        return seq_str in sentence_str
    
    def __all_sentences_with_seq(self, seq: List[str]) -> List[List[str]]:
        """Finds all sentences that contain a given sequence."""
        all_sentences = []
        for sentence in self.__preprocessed_sentences:
            if self.__is_seq_in_sentence_(seq, sentence): 
                all_sentences.append(sentence) 
        if all_sentences == []: return [[]]
        return sorted(all_sentences)

    def preprocess_k_seq_data(self) -> Dict[str, List[List[str]]]:
        """Processes all query sequences and finds their matching sentences."""
        try:
            result = {}
            for seq in self.__pro_k_seq:
                sentences_with_seq = self.__all_sentences_with_seq(seq)
                if sentences_with_seq != [[]]: result[" ".join(seq)] = sentences_with_seq
            return dict(sorted(result.items()))
        except Exception as e:
            print(f"Error in preprocess_k_seq_data: {e}")
            return {}

    def task_4_format(self) -> Dict[str, Dict[str, any]]:
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
            print(f"Error in task_4_format: {e}")
