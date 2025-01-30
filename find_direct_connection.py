from typing import Dict, List
from count_people_mentions import CountPeopleMentions
from itertools import combinations

# class Person:
#     def __init__(self):
#         pass

# class Connection:
#     def __init__(self):
#         pass

# class PeopleConnections:
#     def __init__(self):
#         self.__people = None
#         self.__connections = None

class FindDirectConnection:
    def __init__(self, preprocessed_sentences, preprocessed_people, window_size, threshold):
        # בדיקות ושגיאות על ערכים לא תקינים
        self.__preprocessed_sentences = preprocessed_sentences
        self.__preprocessed_people = preprocessed_people
        self.__window_size = window_size
        self.__threshold = threshold

    def create_people_dict(self) -> Dict[str, List[int]]:
        people_dict = {}
        for person in self.__preprocessed_people:
            people_dict[" ".join(person[0])] = []
        return people_dict

    def get_mentions_in_sentence(self, sentence) -> Dict[str, int]:
        return CountPeopleMentions(self.__preprocessed_people, [sentence]).count_people_mentions()

    def get_all_mentions(self) -> Dict[str, List[int]]:
        people_mentions_dict: Dict[str, List[int]] = self.create_people_dict()
        for sentence in self.__preprocessed_sentences:
            mentions = self.get_mentions_in_sentence(sentence) # Dict[str, int]
            for person in people_mentions_dict:
                if person in mentions:
                    people_mentions_dict[person].append(mentions[person])
                else:
                    people_mentions_dict[person].append(0)
        return people_mentions_dict
    
    def mentioned_people_in_window(self, people_mentions: Dict[str, List[int]], i: int) -> List[str]:
        people = []
        for name, mentions in people_mentions.items():
            if sum(mentions[i:i + self.__window_size]) >= self.__threshold:
                print(i, name, sum(mentions[i:i + self.__window_size]))
                people.append(name)
        return people
    
    def find_connections(self) -> List[List[List[str]]]:
        all_pairs = set()
        people_mentions = self.get_all_mentions()
        for i in range(len(self.__preprocessed_sentences) - self.__window_size + 1):
            mentioned_people_in_window: List[str] = self.mentioned_people_in_window(people_mentions, i)
            all_pairs.update(combinations(mentioned_people_in_window, 2))
            print("all_pairs: ", all_pairs)
        return sorted([sorted(name.split() for name in pair) for pair in all_pairs])

    def to_dict_6(self) -> Dict[str, Dict[str, any]]:
        try:
            return {
                "Question 6": {
                    "Pair Matches": self.find_connections()
                }
            }
        except Exception as e:
            print(f"Error: {e}")


    def find_indirect_connections(self):
        pass


    def to_dict_7(self) -> Dict[str, Dict[str, any]]:
        try:
            return {
                "Question 7": {
                    "Pair Matches": self.find_connections()
                }
            }
        except Exception as e:
            print(f"Error: {e}")

        
        