from typing import Dict, List
from k_seq import KSeq
import utils


class CountPeopleMentions:
    def __init__(self, preprocess_people, preprocess_sentences): # k_seq: Dict[str, Dict[str, int]]
        self.__preprocess_people = preprocess_people
        self.__preprocess_sentences = preprocess_sentences
        self.__k_seq = self.get_seqs_count()

    def get_seqs_count(self) -> Dict[str, Dict[str, int]]:
        longest_name = 0
        # preprocess_object.get_longest_main_name_len()
        for person in self.__preprocess_people:
            if len(person[0]) > longest_name: longest_name = len(person[0])  # error it its not exist
        x = KSeq(self.__preprocess_sentences, longest_name).count_sequences_len_k()
        return x 

    def get_q_seq(self, n: int) -> Dict[str, int]:
        return self.__k_seq.get(f"{n}_seq", {}) # error? instead of {}

    def get_name_count(self, name: List[str]) -> int:
        full_name = " ".join(name)
        q_seq = self.get_q_seq(len(name))
        return q_seq.get(full_name, 0)
    
    def count_person(self, person: List[List[str]]) -> int:
        count = 0
        main_name = person[0]
        nicknames = person[1]
        for name in main_name:
            # print("name: ", name)
            count += self.get_name_count([name])
            if self.get_name_count([name]): print('self.get_name_count([name]): ', name, self.get_name_count([name]))
        for nickname in nicknames:
            # print("nickname: ", nickname)
            count += self.get_name_count(nickname)
            if self.get_name_count([name]):  print("self.get_name_count(nickname): ", nickname, self.get_name_count(nickname))
        return count

    def count_people_mentions(self) -> Dict[str, int]:
        people_mentions = {}
        for person in self.__preprocess_people:
            count = self.count_person(person)
            # print("person, count: ", person, count)
            if count:
                people_mentions[" ".join(person[0])] = count
                # print(": ", person[0], count)
        # return sorted(people_mentions, key=lambda x: x[0]) # if people_mentions else []
        x = dict(sorted(people_mentions.items())) #, key=lambda x: x[0])
        print("x: ", x)
        return x 
    
    def to_dict(self) -> Dict[str, Dict[str, any]]:
        res = [[key, value] for key, value in self.count_people_mentions().items()]
        return {
            "Question 3": {
                "Name Mentions": res,
            }
        }
    
    def __str__(self):
        return utils.to_json_str(self.to_dict())
    