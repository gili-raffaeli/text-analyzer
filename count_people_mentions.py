from typing import Dict, List
from count_words_seq import CountWordsSeq


class CountPeopleMentions:
    """The CountPeopleMentions class processes a list of people (with their names and nicknames) and a list of sentences to count how frequently each person's name or nickname appears in the text."""
    
    def __init__(self, preprocess_people, preprocess_sentences):
        """
        Parameters:
            preprocess_people (List[List[List[str]]]): A list where each person is represented as a list of two lists: main name and nicknames.
            preprocess_sentences (List[str]): A list of sentences (strings) to analyze for name occurrences.
        """
        try:
            # if not utils.is_processed_people_type(preprocess_people): raise TypeError # slower?
            self.__preprocess_people = preprocess_people
            # if not utils.is_processed_sentences_type(preprocess_sentences): raise TypeError # slower?
            self.__preprocess_sentences = preprocess_sentences
            self.__longest_name_len = self.__get_longest_name_len()
            self.__k_seq = self.__get_seqs_count() or {}
        except TypeError as e:
            print("Invalid Parameter Type: ", e)
        except Exception as e:
            print(f"Error during CountPeopleMentions initialization: {e}")

    def __get_longest_name_len(self) -> int:
        """Finds the length of the longest full name in preprocess_people."""
        return max((len(person[0]) for person in self.__preprocess_people), default=0)

    def __get_seqs_count(self) -> Dict[str, Dict[str, int]]:
        """Uses CountWordsSeq to extract sequences of words from preprocess_sentences, returning a dictionary with name sequences and their counts."""
        try:
            return CountWordsSeq(self.__preprocess_sentences, self.__longest_name_len).count_sequences_len_k()
        except Exception as e:
            print(f"Error in get_seqs_count: {e}")
            return {}

    def __get_name_count(self, name: List[str]) -> int:
        """Looks up the occurrence count of a given name (or nickname) in the precomputed sequences."""
        full_name = " ".join(name)
        q_seq = self.__k_seq.get(f"{len(name)}_seq", {})
        return q_seq.get(full_name, 0)
    
    def __count_person(self, person: List[List[str]]) -> int:
        """Counts how many times a person's main names and nicknames appear in the sentences."""
        count = 0
        main_name = person[0]
        nicknames = person[1]
        for name in main_name:
            count += self.__get_name_count([name])
        for nickname in nicknames:
            count += self.__get_name_count(nickname)
        return count

    def count_people_mentions(self) -> Dict[str, int]:
        """Returns a dictionary with full names as keys and their occurrence counts as values."""
        try:
            people_mentions = {}
            for person in self.__preprocess_people:
                count = self.__count_person(person)
                if count:
                    people_mentions[" ".join(person[0])] = count
            return dict(sorted(people_mentions.items()))
        except Exception as e:
            print(f"Error in count_people_mentions: {e}")
             
    def task_3_format(self) -> Dict[str, Dict[str, any]]:
        """Formats the results for "Question 3", returning a nested dictionary with name mentions."""
        try:
            res = [[key, value] for key, value in self.count_people_mentions().items()]
            return {
                "Question 3": {
                    "Name Mentions": res,
                }
            }
        except Exception as e:
            print(f"Error in task_3_format: {e}")
    