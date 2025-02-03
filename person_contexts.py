from typing import Any, Dict, List
from count_words_seq import CountWordsSeq
from search_engine import SearchEngine
import utils


class PersonContexts:
    """Extracts contextual k-sequences for people in tokenized sentences."""

    def __init__(self, preprocess_sentences, preprocess_people, sequence_length: int):
        self.__preprocess_sentences = preprocess_sentences
        self.__preprocess_people = preprocess_people
        self.__sequence_length = sequence_length

    def __get_person_names(self, person: List[List[Any]]) -> List[List[str]]:
        """Extracts all variations of a person's name (main name and nicknames)."""
        return [[part_main_name] for part_main_name in person[0]] + person[1]
    
    def __make_k_seq_of_sentences(self, sentences: List[str]):
        """"Creates k-sequence counts from given sentences."""
        try:
            return CountWordsSeq(sentences, self.__sequence_length).count_sequences_len_k()
        except Exception as e:
                print("make_k_seq_of_sentences failed: ", e)
        
    def __find_people_context(self):
        """Finds context sentences for each person and extracts k-sequences from them."""
        try:
            result = []
            for person in self.__preprocess_people:
                person_names = self.__get_person_names(person)
                search_engine = SearchEngine(self.__preprocess_sentences, person_names)
                person_data = search_engine.preprocess_k_seq_data()

                person_sentences = [sentence for sentences in person_data.values() for sentence in sentences]
                if not person_sentences: continue
                data = self.__make_k_seq_of_sentences(person_sentences)
                
                all_sequences = []
                for seq_key in data:
                    for sequence in data[seq_key].keys():
                        all_sequences.append(sequence.split())
                all_sequences = sorted(all_sequences, key=lambda x: tuple(x))
                result.append([" ".join(person[0]), all_sequences])
                
            return sorted(result, key=lambda x: x[0]) 
        except Exception as e:
            print("find_people_context failed: ", e)

    def task_5_format(self) -> Dict[str, Dict[str, any]]:
        """Converts the preprocessed data into a task_5_format format."""
        try:
            return {
                "Question 5": {
                    "Person Contexts and K-Seqs": self.__find_people_context()
                }
            }
        except Exception as e:
            print(f"Error in task_5_format: {e}")
