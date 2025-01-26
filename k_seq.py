from typing import Dict, List
import utils

class KSeq:
    """
    A class for extracting and counting sequences of words from preprocessed sentences.
    Attributes:
        __preprocessed_sentences (List[List[str]]): A list of sentences, where each sentence is a list of words.
        __sequence_length (int): The length of the sequences to extract.
    """

    def __init__(self, preprocessed_sentences: List[List[str]], sequence_length: int):
        try:
            if not (isinstance(sequence_length, int) and sequence_length > 0): raise ValueError 
            self.__sequence_length = sequence_length
            if not utils.is_type_List_List_str(preprocessed_sentences): raise ValueError
            self.__preprocessed_sentences = preprocessed_sentences
        except ValueError as e:
            print("Invalid Parameter: ", e)
        except Exception as e:
            print(e)

    def __count_sequence_in_sentence(self, sequence: List[str], sentence: List[str]) -> int:
        """Counts occurrences of a specific sequence in a single sentence."""
        if len(sentence) < len(sequence): return 0
        sequence_count = 0
        for i in range(len(sentence) - len(sequence) + 1):
            if sequence == sentence[i:i+len(sequence)]:
                sequence_count += 1
        return sequence_count

    def __cont_sequence(self, sequence: List[str]) -> int:
        """Counts the occurrences of a sequence across all sentences."""
        sequence_count = 0
        for sentence in self.__preprocessed_sentences:
            sequence_count += self.__count_sequence_in_sentence(sequence, sentence)
        return sequence_count
    
    def __get_sequences_of_length(self, seq_len: int) -> List[List[str]]:
        """Extracts all unique sequences of the specified length from all sentences."""
        all_sequences = set()
        for sentence in self.__preprocessed_sentences:
            if len(sentence) < seq_len: continue
            for i in range(len(sentence) - seq_len + 1):
                all_sequences.add(tuple(sentence[i:i+seq_len]))
        all_sequences_list = [list(seq) for seq in all_sequences]
        if len(all_sequences_list) == 0: return [[]]
        return all_sequences_list

    def __get_n_seq_counts(self, seq_len: int) -> Dict[str, int]:
        """Returns a dictionary of sequence counts for sequences of a given length."""
        n_seq_counts = {}
        sequences_len_n = self.__get_sequences_of_length(seq_len)
        for sequence_len_n in sequences_len_n:
            sequence_count = self.__cont_sequence(sequence_len_n)
            n_seq_counts[" ".join(sequence_len_n)] = sequence_count
        return dict(sorted(n_seq_counts.items()))
    
    def count_sequences_len_k(self) -> Dict[str, Dict[str, int]]:
        """Returns a dictionary of sequence counts for sequence lengths from 1 to `__sequence_length`."""
        try:
            k_seq = {}
            for k in range(1, self.__sequence_length + 1):
                k_seq[f"{k}_seq"] = self.__get_n_seq_counts(k)
            return k_seq
        except Exception as e:
            print(e)
            return None
    
    def get_format_count_seq(self) -> Dict:
        """Formats the sequence counts into a specific structure for output."""
        try:
            list_seq_count = []
            k_seq = self.count_sequences_len_k()
            if k_seq == None: raise Exception # handle this better?
            for k_seq_type, n_seq_counts in k_seq.items():
                n_seq_list = utils.turn_Dict_str_any_to_List_any(n_seq_counts)
                list_seq_count.append([k_seq_type, n_seq_list])

            return {
                "Question 2": {
                    f"{self.__sequence_length}-Seq Counts":  list_seq_count
                }
            }
        except Exception as e:
            print(e)
            return None
    
    def __str__(self):
        """Returns the string representation of the formatted sequence counts."""
        return utils.to_json_str(self.get_format_count_seq())
    