from typing import Any, Dict, List
from k_seq import KSeq
from search_engine import SearchEngine
import utils


class PersonContextsAndKSeqs:
    def __init__(self, preprocess_sentences, preprocess_people, sequence_length: int):
        self.__preprocess_sentences = preprocess_sentences
        self.__preprocess_people = preprocess_people
        self.__sequence_length = sequence_length

    def get_person_names(self, person: List[List[Any]]) -> List[List[str]]:
        return [[part_main_name] for part_main_name in person[0]] + person[1]
    
    def make_k_seq_of_sentences(self, sentences: List[str]):
        try:
            return KSeq(sentences, self.__sequence_length).count_sequences_len_k()
        except Exception as e:
                print("make_k_seq_of_sentences failed: ", e)
        
    def find_people_context(self):
        try:
            result = []
            for person in self.__preprocess_people:
                person_names = self.get_person_names(person)
                search_engine = SearchEngine(self.__preprocess_sentences, person_names)
                person_data = search_engine.preprocess_k_seq_data()
                person_sentences = [sentence for sentences in person_data.values() for sentence in sentences]
                if not person_sentences: continue
                data = self.make_k_seq_of_sentences(person_sentences)
                all_sequences = []
                for seq_key in data:
                    for sequence in data[seq_key].keys():
                        all_sequences.append(sequence.split())
                all_sequences = sorted(all_sequences, key=lambda x: tuple(x))
                result.append([" ".join(person[0]), all_sequences])
                
            return sorted(result, key=lambda x: x[0]) 
        except Exception as e:
            print("find_people_context failed: ", e)

    def to_dict(self) -> Dict[str, Dict[str, any]]:
        """Converts the preprocessed data into a dictionary format."""
        try:
            return {
                "Question 5": {
                    "Person Contexts and K-Seqs": self.find_people_context()
                }
            }
        except Exception as e:
            print(f"Error: {e}")

    def __str__(self):
        """Returns the JSON string representation of the object."""
        return utils.to_json_str(self.to_dict())
    