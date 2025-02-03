#!/usr/bin/env python3

import argparse
from pathlib import Path
from count_people_mentions import CountPeopleMentions
from count_words_seq import CountWordsSeq
from find_connections import FindConnections
from person_contexts import PersonContexts
from preprocess import Preprocess
from search_engine import SearchEngine
import utils


def readargs(args=None):
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

def int_validation(var: any) -> bool:
    if var: 
        if type(var) != int or var < 1: 
            print("invalid input")
            return False
    return True

def validate_file_exists(file_path: any) -> bool:
    if type(file_path) != str:
        print("invalid input")
        return False
    if not Path(file_path).exists():
        print("invalid input")
        return False
    return True

def validate_args(args) -> bool:
    if args.preprocessed == None:
        if not validate_file_exists(args.removewords) or not validate_file_exists(args.sentences): return False
        if args.task not in ['2', '4'] or args.names != None: 
            if not validate_file_exists(args.names): return False
    else:
        if not validate_file_exists(args.preprocessed): return False

    if args.task == '1': pass
    elif args.task == '2':
        if not int_validation(args.maxk): return False
    elif args.task == '3': pass
    elif args.task == '4':
        if not validate_file_exists(args.qsek_query_path): return False 
    elif args.task == '5':
        if not int_validation(args.maxk): return False
    elif args.task == '6':
        if not int_validation(args.windowsize) or not int_validation(args.threshold): return False
    elif args.task in ['7', '8']:
        if not int_validation(args.windowsize) or not int_validation(args.threshold): return False
        if not validate_file_exists(args.pairs): return False
        if args.task == '7':
            if not int_validation(args.maximal_distance): return False
        elif args.task == '8':
            if not int_validation(args.fixed_length): return False
    elif args.task == '9': pass 
    else:
        print("invalid input")
        return False
    return True

def json_print(object):
    print(utils.to_json_str(object))

def main():
    args = readargs()
    if not validate_args(args): return

    if args.preprocessed == None:
        processed_object = Preprocess(args.removewords, args.sentences, args.names)
        processed_data = processed_object.task_1_format()
    else:
        processed_data = utils.read_json_file(args.preprocessed)
        if not processed_data: return

    try:    
        processed_sentences = processed_data["Question 1"]["Processed Sentences"]
        processed_names = processed_data["Question 1"]["Processed Names"]
    except Exception as e:
        print(f'Error in getting processed_sentences processed_names: {e}')
        return
    
    if args.task == '1': json_print(processed_data)
    elif args.task == '2': json_print(CountWordsSeq(processed_sentences, args.maxk).task_2_format())
    elif args.task == '3': json_print(CountPeopleMentions(processed_names, processed_sentences).task_3_format())
    elif args.task == '4':
        query_data = utils.read_json_file(args.qsek_query_path)
        kseq_query_keys = query_data["keys"] # processed_object.clean_List_List_str(...) 
        json_print(SearchEngine(processed_sentences, kseq_query_keys).task_4_format())
    elif args.task == '5': json_print(PersonContexts(processed_sentences, processed_names, args.maxk).task_5_format())
    elif args.task == '6': json_print(FindConnections(processed_sentences, processed_names, args.windowsize, args.threshold).task_6_format())
    elif args.task in ['7', '8']:
        query_data = utils.read_json_file(args.pairs)
        keys = sorted([sorted(name for name in pair) for pair in query_data["keys"]])
        find_connections = FindConnections(processed_sentences, processed_names, args.windowsize, args.threshold)
        if args.task == '7': json_print(find_connections.task_7_8_format(keys, maximal_distance = args.maximal_distance))
        elif args.task == '8': json_print(find_connections.task_7_8_format(keys, fixed_length = args.fixed_length))
    elif args.task == '9': pass 
    else: print("invalid input")

if __name__=="__main__":
    main()
