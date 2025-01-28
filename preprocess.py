from typing import Any, Dict, List
import utils
import pandas as pd
import string
import re


class Preprocess:
    """This class provides methods to preprocess text data, remove unwanted words, clean sentences, and handle people data (main names and nicknames)."""
    def __init__(self, remove_words_path, sentences_path, people_path = None):
        try:
            self.__used_names = []
            self.__longest_main_name_len = 0
            self.__preprocessed_remove_words = self.__preprocess_remove_words(remove_words_path)
            self.__preprocessed_sentences = self.__preprocess_sentences(sentences_path)
            if people_path != None: 
                self.__preprocessed_people = self.__preprocess_people(people_path)
            else:
                self.__preprocessed_people = None
        except Exception as e:
            print(f"Error during initialization: {e}")

    def get_preprocessed_remove_words(self):
        """Returns the set of words that will be removed from the text."""
        return self.__preprocessed_remove_words
    
    def get_preprocessed_sentences(self):
        """Returns the preprocessed sentences."""
        return self.__preprocessed_sentences
    
    def get_preprocessed_people(self):
        """Returns the preprocessed people data."""
        return self.__preprocessed_people
    
    def get_longest_main_name_len(self) -> int:
        """Returns the length of the longest main name found in the people data."""
        return self.__longest_main_name_len

    def __load_csv_file(self, file_path):
        """Loads a CSV file and returns the data."""
        try:
            data_file = pd.read_csv(file_path)
            if data_file.empty or data_file.columns.empty:
                raise ValueError(f"'{file_path}' is empty or has no valid columns.")
            return data_file
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Unexpected error: {e}")
        return None

    def __remove_punctuation(self, text: str) -> str:
        """Removes punctuation from the given text."""
        translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
        return text.translate(translator)
    
    def __make_single_spaces(self, text: str) -> str:
        """Replaces multiple spaces with a single space in the given text."""
        return re.sub(r'\s+', ' ', text)

    def __clean_text(self, text: str) -> List[str]:
        """Cleans the text by removing punctuation, making spaces consistent, and converting to lowercase."""
        removed_text = self.__remove_punctuation(text)
        text_with_single_spaces = self.__make_single_spaces(removed_text)
        return text_with_single_spaces.lower().strip().split()

    def __process_single_column_file(self, file_path: str) -> List[str]:
        """Processes a CSV file with a single column and returns a list of cleaned words."""
        df = self.__load_csv_file(file_path) #here?
        first_column = df.iloc[:, 0]
        return (
            first_column.astype(str)
            .apply(self.__clean_text)
            .tolist()
        )
    
    def __preprocess_remove_words(self, remove_words_path: str) -> List[str]:
        """Loads and processes the words that need to be removed from the text."""
        word_lists = self.__process_single_column_file(remove_words_path)
        return set([word for sublist in word_lists for word in sublist])
    
    def __remove_words(self, words: List[str]) -> List[str]:
            """Removes unwanted words from a list of words."""
            if not words: return []
            return [word for word in words if word not in self.__preprocessed_remove_words]

    def __preprocess_sentences(self, sentences_path: str) -> List[List[str]]:
        """Processes sentences by cleaning them and removing unwanted words."""
        try:
            cleaned_sentences = self.__process_single_column_file(sentences_path)
            preprocess_sentences = []
            # remove unwanted words
            for sentence in cleaned_sentences:
                remove_sentence = self.__remove_words(sentence)
                if remove_sentence: preprocess_sentences.append(remove_sentence)
            return preprocess_sentences
        except Exception as e:
            print(f"Error processing sentences: {e}")
    
    def __is_name_used(self, name: List[str]) -> bool:
        """Checks if the given name has already been used (to avoid duplicates)."""
        return name in self.__used_names 

    def __preprocess_people(self, people_path: str):
        """Processes the people data by cleaning names and nicknames, ensuring no duplicates."""
        try:
            people_data = self.__load_csv_file(people_path)
            people_names = []
            for index, row in people_data.iterrows():
                main_name = row.iloc[0]
                nicknames = row.iloc[1]
                if not isinstance(main_name, str): continue
                main_name_clean = self.__remove_words(self.__clean_text(main_name))
                if self.__is_name_used(main_name_clean): continue
                self.__used_names.append(main_name_clean)
                self.__longest_main_name_len = max(self.__longest_main_name_len, len(main_name_clean)) # save longest name length

                person_names = [main_name_clean]
                all_nicknames = []
                if isinstance(nicknames, str):
                    temp_used_names = []
                    for nickname in nicknames.split(','):
                        cleaned_nickname = self.__clean_text(nickname)
                        fixed_nickname = self.__remove_words(cleaned_nickname)
                        if not self.__is_name_used(fixed_nickname):
                            all_nicknames.append(fixed_nickname)
                            temp_used_names.append(fixed_nickname)        
                    self.__used_names.extend(temp_used_names)
                person_names.append(all_nicknames)
                people_names.append(person_names)
            return people_names
        except Exception as e:
            print(f"Error processing people data: {e}")

    def clean_List_List_str(self, object: List[List[str]]) -> List[List[str]]:
        """Processes a list of lists of strings by cleaning each word and removing unwanted words."""
        try:
            cleaned_object = []
            for sub_list in object:
                if not sub_list: continue
                cleaned_sub_list = []
                for word in sub_list:
                    if not word: continue
                    cleaned_word = self.__clean_text(word)
                    filtered_word = self.__remove_words(cleaned_word)
                    cleaned_sub_list.extend(filtered_word)
                if cleaned_sub_list: cleaned_object.append(cleaned_sub_list)
            return cleaned_object
        except Exception as e:
            print(f"Error: {e}")
            return None

    def to_dict(self) -> Dict[str, Dict[str, any]]:
        """Converts the preprocessed data into a dictionary format."""
        try:
            return {
                "Question 1": {
                    "Processed Sentences": self.__preprocessed_sentences,
                    "Processed Names": self.__preprocessed_people,
                }
            }
        except Exception as e:
            print(f"Error: {e}")
    
    def __str__(self):
        """Returns the JSON string representation of the object."""
        return utils.to_json_str(self.to_dict())
    