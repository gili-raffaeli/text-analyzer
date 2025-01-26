from typing import Dict, List
import utils


class CountPersonMentions:
    def __init__(self, preprocess_people, k_seq: Dict[str, Dict[str, int]]):
        self.__preprocess_people = preprocess_people
        self.__k_seq = k_seq

    def get_q_seq(self, n: int) -> Dict[str, int]:
        return self.__k_seq.get(f"{n}_seq", {}) # error? instead of {}

    def get_name_count(self, name: List[str]) -> int:
        full_name = " ".join(name)
        q_seq = self.get_q_seq(len(name))
        return q_seq.get(full_name, 0)
    
    def count_person(self, person: List[List[str]]):
        count = 0
        main_name = person[0]
        nicknames = person[1]
        for name in main_name:
            count += self.get_name_count([name])
        for nickname in nicknames:
            count += self.get_name_count(nickname)
        count -= self.get_name_count(main_name) * (len(main_name) - 1)
        return count

    def main_name_count(self):
        people_mentions = []
        for person in self.__preprocess_people:
            count = self.count_person(person)
            if count:
                people_mentions.append([" ".join(person[0]), count])
        return sorted(people_mentions, key=lambda x: x[0]) # if people_mentions else []
    
    def to_dict(self) -> Dict:
        return {
            "Question 3": {
                "Name Mentions": self.main_name_count(),
            }
        }
    
    def __str__(self):
        return utils.to_json_str(self.to_dict())
    