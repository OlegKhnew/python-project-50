#!/usr/bin/env python3

import json


def get_output(file1_dict, file2_dict):
    keys1 = list(file1_dict.keys())
    keys2 = list(file2_dict.keys())
    sorted_items = sorted(set(keys1 + keys2))
    output = "{\n"
    for item in sorted_items:
        if file1_dict.get(item) and \
                file2_dict.get(item) and \
                file1_dict[item] == file2_dict[item]:
            output += (f'  {item}: {str(file1_dict[item])}\n')
        else:
            if file1_dict.get(item):
                output += (f'- {item}: {str(file1_dict[item])}\n')
            if file2_dict.get(item):
                output += (f'+ {item}: {str(file2_dict[item])}\n')
    output += '}'
    return output


def generate_diff(file_path1, file_path2):
    file1_dict = json.load(open(file_path1))
    file2_dict = json.load(open(file_path2))
    for d in (file1_dict, file2_dict):
        for element in d:
            d[element] = str(
                d[element]).replace('False', 'false').replace('True', 'true')
    result = get_output(file1_dict, file2_dict)
    return result
