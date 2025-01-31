from collections import Counter
from typing import Dict, List
from count_people_mentions import CountPeopleMentions
from itertools import combinations

class Person:
    def __init__(self, name):
        self.__name = name
        self.__neighbors = []

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
            if sum(mentions[i:i + self.__window_size]):
                people.append(name)
        return people
    
    # if sum(mentions[i:i + self.__window_size]) >= self.__threshold:

    
    def find_connections(self) -> set[tuple[str]]:
        all_pairs = []
        people_mentions = self.get_all_mentions()
        for i in range(len(self.__preprocessed_sentences) - self.__window_size + 1):
            mentioned_people_in_window: List[str] = self.mentioned_people_in_window(people_mentions, i)
            all_pairs.extend(combinations(mentioned_people_in_window, 2))
        print("all_pairs: ", all_pairs)
        pair_counts = dict(Counter(all_pairs))  # Count occurrences of each pair
        right_pairs = []
        for pair, amount in pair_counts.items():
            if amount >= self.__threshold:
                right_pairs.append(pair)
        return right_pairs

    def to_dict_6(self) -> Dict[str, Dict[str, any]]:
        all_pairs = self.find_connections()
        formated = sorted([sorted(name.split() for name in pair) for pair in all_pairs])
        try:
            return {
                "Question 6": {
                    "Pair Matches": formated
                }
            }
        except Exception as e:
            print(f"Error: {e}")


    def create_people_nodes(self):
        connections = self.find_connections()
        people_connections_dict = {}
        for pair in connections:
            p1, p2 = pair[0], pair[1]
            if p1 not in people_connections_dict.keys():
                people_connections_dict[p1] = set()
            people_connections_dict[p1].add(p2)
            if p2 not in people_connections_dict:
                people_connections_dict[p2] = set()
            people_connections_dict[p2].add(p1)
        print(people_connections_dict)
        return people_connections_dict
    
    def check_for_connection(self, current: str, destination: str, checked: List[str], people_connections_dict) -> bool:
        if current == destination:
            return True
        if current not in people_connections_dict.keys(): return False
        connected = people_connections_dict[current]
        for connect in connected:
            if connect not in checked:
                found_connection = self.check_for_connection(connect, destination, checked + [current], people_connections_dict)
                if found_connection: return True
        return False
    
    def check_connections(self, pairs_to_check: List[List[str]]):
        check_connection = self.create_people_nodes()
        result = []
        for pair in pairs_to_check:
            is_connections = self.check_for_connection(pair[0], pair[1], [], check_connection)
            result.append(pair + [is_connections])
        return result
            

    def to_dict_7(self, pairs_to_check: List[List[str]]) -> Dict[str, Dict[str, any]]:
        try:
            return {
                "Question 7": {
                    "Pair Matches": self.check_connections(pairs_to_check)
                }
            }
        except Exception as e:
            print(f"Error: {e}")

        
# לשנות כך ש6 ייצור את המערך?