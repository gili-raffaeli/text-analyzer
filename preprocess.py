import json
import re
import string
from typing import Dict, List
import pandas as pd

class Preprocess:
    def __init__(self, sentences_path, people_path, remove_words_path): #changed to path
        try:
            self.__used_names = []
            self.__max_main_name_len = 0
            self.__remove_words = self.preprocess_remove_words(remove_words_path)
            self.__sentences = self.preprocess_sentences(sentences_path)
            self.__people = self.preprocess_people(people_path)
        except Exception as e:
            print(f"Error during initialization: {e}")

    def get_remove_words(self):
        return self.__remove_words
    
    def get_sentences(self):
        return self.__sentences
    
    def get_people(self):
        return self.__people
    
    def get_max_main_name_len(self) -> int:
        return self.__max_main_name_len

    def load_csv_file(self, file_path):
        try:
            # print('11')
            # print(file_path)
            data_file = pd.read_csv(file_path)
            # print('12')
            if data_file.empty or data_file.columns.empty: # do something else with this
                # print('13')
                print(f"Error: '{file_path}' is empty or has no valid columns.")
            # print('14')
            return data_file
        except FileNotFoundError as e1:
            print(f"FileNotFoundError: {e1}")
        except Exception as e2:
            print(f"Error: {e2}")

    def remove_punctuation(self, text: str) -> str:
        translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
        return text.translate(translator)
    
    def make_single_spaces(self, text: str) -> str:
        return re.sub(r'\s+', ' ', text)

    def clean_text(self, text: str) -> List[str]:
        removed_text = self.remove_punctuation(text)
        text_with_single_spaces = self.make_single_spaces(removed_text)
        return text_with_single_spaces.lower().strip().split()

    def preprocess_one_col_file(self, remove_words_path: str) -> List[str]:
        # print('a')
        df = self.load_csv_file(remove_words_path)
        # print('b')
        first_column = df.iloc[:, 0]
        # print('c')
        return (
            first_column.astype(str)
            .apply(self.clean_text)
            .tolist()
        )
    
    def preprocess_remove_words(self, remove_words_path: str) -> List[str]:
        word_lists = self.preprocess_one_col_file(remove_words_path)
        return set([word for sublist in word_lists for word in sublist])
    
    def remove_words(self, words: List[str]) -> List[str]:
            return [word for word in words if word not in self.__remove_words] if words else []

    def preprocess_sentences(self, sentences_path: str) -> List[List[str]]:
        try:
            # print('1')
            cleaned_sentences = self.preprocess_one_col_file(sentences_path)
            # print('2')
            preprocess_sentences = []
            # remove unwanted words
            for sentence in cleaned_sentences:
                remove_sentence = self.remove_words(sentence)
                if remove_sentence: preprocess_sentences.append(remove_sentence)
            return preprocess_sentences
        except Exception as e:
            print(f"Error processing sentences: {e}")
    
    def is_name_used(self, name: List[str]) -> bool:
        return name in self.__used_names 

    def preprocess_people(self, people_path: str):
        people_data = self.load_csv_file(people_path)
        people_names = []
        for index, row in people_data.iterrows():
            main_name = row.iloc[0]
            nicknames = row.iloc[1]
            if not isinstance(main_name, str): continue

            cleaned_main_name = self.clean_text(main_name)
            fixed_main_name = self.remove_words(cleaned_main_name)
            if self.is_name_used(fixed_main_name): continue  

            person_names = [fixed_main_name]
            self.__used_names.append(fixed_main_name)
            if len(fixed_main_name) > self.__max_main_name_len: self.__max_main_name_len = len(fixed_main_name) 

            all_nicknames = []
            if isinstance(nicknames, str):
                temp_used_names = []
                for nickname in nicknames.split(','):
                    cleaned_nickname = self.clean_text(nickname)
                    fixed_nickname = self.remove_words(cleaned_nickname)
                    if not self.is_name_used(fixed_nickname):
                        all_nicknames.append(fixed_nickname)
                        temp_used_names.append(fixed_nickname)        
                self.__used_names.extend(temp_used_names)
            person_names.append(all_nicknames)
            people_names.append(person_names)
        return people_names

    def to_dict(self) -> Dict:
        return {
            "Question 1": {
                "Processed Sentences": self.__sentences,
                "Processed Names": self.__people,
            }
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def __str__(self):
        return str(self.to_json())
    



## להפריד עיבוד משפטים מעיבוד שמות