#!/usr/bin/env python3

import argparse
from count_people_mentions import CountPeopleMentions
from count_words_seq import CountWordsSeq
from people_connections import PeopleConnections
from person_contexts import PersonContexts
from preprocess import Preprocess
from search_engine import SearchEngine
from sentences_connections import SentencesConnections
from utils import validate_args, read_json_file, json_print, read_json_file


def readargs(args=None):
    """Parses command-line arguments for the text analysis project."""
    parser = argparse.ArgumentParser(
        prog='Text Analyzer project',
    )
    # General arguments
    parser.add_argument('-t', '--task',
                        help="task number",
                        required=True
                        )
    parser.add_argument('-s', '--sentences',
                        help="Sentence file path",
                        )
    parser.add_argument('-n', '--names',
                        help="Names file path",
                        )
    parser.add_argument('-r', '--removewords',
                        help="Words to remove file path",
                        )
    parser.add_argument('-p', '--preprocessed',
                        action='append',
                        help="json with preprocessed data",
                        )
    # Task specific arguments
    parser.add_argument('--maxk',
                        type=int,
                        help="Max k",
                        )
    parser.add_argument('--fixed_length',
                        type=int,
                        help="fixed length to find",
                        )
    parser.add_argument('--windowsize',
                        type=int,
                        help="Window size",
                        )
    parser.add_argument('--pairs',
                        help="json file with list of pairs",
                        )
    parser.add_argument('--threshold',
                        type=int,
                        help="graph connection threshold",
                        )
    parser.add_argument('--maximal_distance',
                        type=int,
                        help="maximal distance between nodes in graph",
                        )

    parser.add_argument('--qsek_query_path',
                        help="json file with query path",
                        )
    return parser.parse_args(args)

def main():
    """Main function that reads arguments, validates them, and runs the appropriate task."""
    try: 
        args = readargs()
        if not validate_args(args): return
    except Exception as e:
        print(f"Error with args: {e}")
        return

    try:    
        if args.preprocessed is None or args.task == '1':
            names = args.names if not args.task in ['2', '4', '9'] else None
            processed_object = Preprocess(args.removewords, args.sentences, names)
            processed_data = processed_object.task_1_format()
        else:
            processed_data = read_json_file(args.preprocessed)

        processed_sentences = processed_data["Question 1"]["Processed Sentences"]
        processed_names = processed_data["Question 1"]["Processed Names"]
    except Exception as e:
        print(f'Error in getting processed_sentences and processed_names: {e}')
        return
    
    try:
        if args.task == '1': 
            json_print(processed_data)
        elif args.task == '2': 
            json_print(CountWordsSeq(processed_sentences, args.maxk).task_2_format())
        elif args.task == '3': 
            json_print(CountPeopleMentions(processed_names, processed_sentences).task_3_format())
        elif args.task == '4':
            query_data = read_json_file(args.qsek_query_path)["keys"]
            json_print(SearchEngine(processed_sentences, query_data).task_4_format())
        elif args.task == '5': 
            json_print(PersonContexts(processed_sentences, processed_names, args.maxk).task_5_format())
        elif args.task == '6': 
            json_print(PeopleConnections(processed_sentences, processed_names, args.windowsize, args.threshold).task_6_format())
        elif args.task in ['7', '8']:
            pairs_data = read_json_file(args.pairs)["keys"]
            find_connections = PeopleConnections(processed_sentences, processed_names, args.windowsize, args.threshold)
            if args.task == '7': 
                json_print(find_connections.task_7_8_format(pairs_data, maximal_distance = args.maximal_distance))
            elif args.task == '8': 
                json_print(find_connections.task_7_8_format(pairs_data, fixed_length = args.fixed_length))
        elif args.task == '9': 
            json_print(SentencesConnections(processed_sentences, args.threshold).task_9_format())
        else: print("invalid input")
    except Exception as e:
        print(f"unexpected error {e}")

if __name__=="__main__":
    main()
