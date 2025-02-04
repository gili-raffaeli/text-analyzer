from collections import Counter
from typing import Dict, List, Set, Tuple


class SentencesConnections:
    """
    A class to analyze sentence connections based on shared words.
    Groups sentences that share words frequently above a given threshold.
    """
    def __init__(self, processed_sentences, threshold):
        self.__processed_sentences = processed_sentences
        self.__threshold = threshold

    def __get_all_pairs(self, sentences: List[List[str]]) -> List[Tuple[int, int]]: 
        """Finds all sentence index pairs that share at least one word."""
        sentences_indexes_pairs = []
        for i, sentence in enumerate(sentences):
            checked_words = set()
            for word in sentence:
                if word in checked_words: continue 
                for j in range(i, len(sentences)):
                    if word in sentences[j]:
                        sentences_indexes_pairs.append((i,j))
                checked_words.add(word)
        return sentences_indexes_pairs

    def __find_correct_pairs(self, sentences_indexes_pairs: List[Tuple[int, int]], threshold: int) -> List[Tuple[int, int]]:
        """Filters sentence pairs to retain only those appearing at least `threshold` times."""
        pair_counts = Counter(sentences_indexes_pairs)
        return [pair for pair, count in pair_counts.items() if count >= threshold]

    def __create_sentences_groups(self, sentences: List[List[str]], pairs: List[Tuple[int, int]]) -> List[Set[int]]:
        """Groups sentences based on their connections."""
        groups = []
        for p1, p2 in pairs:
            added_to = -1 #maybe can be better
            for i in range(len(groups)):
                if p1 in groups[i] or p2 in groups[i]:
                    if added_to == -1:
                        groups[i].update([p1, p2])
                        added_to = i
                    else:
                        groups[i].update(groups[added_to])
                        del groups[added_to]
            
            if added_to == -1:
                groups.append(set([p1, p2]))
        all_indices = set(range(len(sentences)))
        grouped_indices = set(i for group in groups for i in group)
        ungrouped = all_indices - grouped_indices
        for i in ungrouped:
            groups.append({i})
        return groups
    
    def __sort_sentences_groups(self, sentences: List[List[str]], index_groups: List[Set[int]]) -> List[List[str]]:
        """Sorts groups by size and lexicographical order."""
        sentence_groups = [sorted([sentences[i] for i in index_group]) for index_group in index_groups]
        return sorted(sentence_groups, key=lambda group: (len(group), group))
    
    def __get_groups(self) -> List[List[any]]:
        """Constructs the final grouped sentence representation."""
        sentences = self.__processed_sentences
        sentences_indexes_pairs = self.__get_all_pairs(sentences)
        right_pairs = self.__find_correct_pairs(sentences_indexes_pairs, self.__threshold)
        groups = self.__create_sentences_groups(sentences, right_pairs)
        sentence_groups = self.__sort_sentences_groups(sentences, groups)
        return [[f"Group {i+1}", group] for i, group in enumerate(sentence_groups)]

    def task_9_format(self) -> Dict[str, Dict[str, List[any]]]:
        """Returns the grouped sentences in the required JSON-like format."""
        try:
            return {
                "Question 9": {
                    "group Matches": self.__get_groups()
                }
            }
        except Exception as e:
            print(f"Error in task_9_format: {e}")