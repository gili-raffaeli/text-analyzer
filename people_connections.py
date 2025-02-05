from collections import Counter
from typing import Dict, List, Optional
from count_people_mentions import CountPeopleMentions
from itertools import combinations

class PeopleConnections:
    def __init__(self, preprocessed_sentences, preprocessed_people, window_size, threshold):
        self.__preprocessed_sentences = preprocessed_sentences
        self.__preprocessed_people = preprocessed_people
        self.__window_size = window_size
        self.__threshold = threshold

    def __get_mentions_in_sentence(self, sentence) -> Dict[str, int]:
        """Returns a dictionary of people mentioned in a sentence with their corresponding mention count."""
        try:
            mentions = CountPeopleMentions(self.__preprocessed_people, [sentence]).count_people_mentions()
            return list(mentions.keys())
        except Exception as e:
            print(f"Error in get_mentions_in_sentence: {e}")

    def __people_mentioned_each_sentence(self) -> List[List[str]]:
        """Processes the preprocessed sentences and returns a list of lists containing the people mentioned in each sentence, identifying sentence by the index."""
        mentioned_people = []
        for sentence in self.__preprocessed_sentences:
            mentions = self.__get_mentions_in_sentence(sentence)
            mentioned_people.append(mentions if mentions else [])
        return mentioned_people
    
    def __mentioned_people_in_window(self, people_mentions: List[List[str]], i: int) -> List[str]:
        """Extracts the people mentioned across a sliding window of sentences starting at index i."""
        people = set()
        for j in range(i, i + self.__window_size):
            people.update(people_mentions[j])
        return list(people)
    
    def __find_pairs(self) -> List[tuple[str, str]]:
        """Identifies pairs of people mentioned together within the sliding window that exceed the mention threshold."""
        all_pairs = []
        people_mentions = self.__people_mentioned_each_sentence()
        for i in range(len(self.__preprocessed_sentences) - self.__window_size + 1):
            mentioned_people_in_window: List[str] = self.__mentioned_people_in_window(people_mentions, i)
            all_pairs.extend(tuple(sorted(pair)) for pair in  combinations(mentioned_people_in_window, 2))
        pair_counts = dict(Counter(all_pairs))  # Count occurrences of each pair
        right_pairs = []
        for pair, amount in pair_counts.items():
            if amount >= self.__threshold:
                right_pairs.append(pair)
        return right_pairs

    def __create_people_connected_dict(self) -> Dict[str, set[str]]:
        """Creates a dictionary of all people connected to each person."""
        try:
            connections = self.__find_pairs()
            people_connections_dict = {}
            for p1, p2 in connections:
                people_connections_dict.setdefault(p1, set()).add(p2)
                people_connections_dict.setdefault(p2, set()).add(p1)
            return people_connections_dict
        except Exception as e:
            print(f"Error in create_people_nodes: {e}")
    
    def __check_for_connection(self, current: str, destination: str, checked: List[str], people_connections_dict: Dict[str, set[str]], maximal_distance: Optional[int], depth: Optional[int]) -> bool:
        """Recursively checks whether there is a path from current to destination in the graph, with a limit on maximal_distance and optional fixed depth."""
        try:
            if depth == 0 or maximal_distance == 0: return False
            if current == destination:
                if depth == None:
                    return True
                else:
                    return depth == 1
            if current not in people_connections_dict.keys(): return False
            connected = people_connections_dict[current]
            for connect in connected:
                if connect not in checked:
                    next_depth = depth - 1 if depth else depth
                    next_maximal_distance = maximal_distance - 1 if maximal_distance else maximal_distance
                    found_connection = self.__check_for_connection(connect, destination, checked + [current], people_connections_dict, next_maximal_distance, next_depth)
                    if found_connection: return True
            return False
        except Exception as e:
            print(f"Error in check_for_connection: {e}")


    

    def __check_connections(self, pairs_to_check: List[List[str]], maximal_distance: Optional[int], fixed_length: Optional[int]) -> List[List[any]]:
        """Checks whether each pair in pairs_to_check is connected within the given maximal_distance or a fixed-length path."""
        try:
            sorted_pairs = sorted([sorted(name for name in pair) for pair in pairs_to_check])
            check_connection = self.__create_people_connected_dict()
            result = []
            for pair in sorted_pairs:
                if pair[0] not in check_connection or pair[1] not in check_connection: 
                    is_connections = False
                else: 
                    is_connections = self.__check_for_connection(pair[0], pair[1], [], check_connection, maximal_distance, fixed_length)
                result.append(pair + [is_connections])
            return result
        except Exception as e:
            print(f"Error in check_connections: {e}")
            
    def task_6_format(self) -> Dict[str, Dict[str, any]]:
        """Formats and returns the pairs of people that are connected based on the mention threshold for Task 6."""
        all_pairs = self.__find_pairs()
        formatted = sorted([sorted(name.split() for name in pair) for pair in all_pairs])
        try:
            return {
                "Question 6": {
                    "Pair Matches": formatted
                }
            }
        except Exception as e:
            print(f"Error in task_6_format: {e}")

    def task_7_8_format(self, pairs_to_check: List[List[str]], maximal_distance: int = None, fixed_length: int = None) -> Dict[str, Dict[str, any]]:
        """Formats and returns the results for Task 7 and 8, determining whether the pairs are connected within a given distance or a fixed-length path."""
        try:
            q_num = 7 if fixed_length == None else 8
            return {
                f"Question {q_num}": {
                    "Pair Matches": self.__check_connections(pairs_to_check, maximal_distance, fixed_length)
                }
            }
        except Exception as e:
            print(f"Error in task_7_8_format: {e}")
