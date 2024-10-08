#!/usr/bin/env python3

from gendiff.parser import parse
from gendiff.formaters.stylish import to_stylish
from gendiff.formaters.plain import to_plain
from gendiff.formaters.json_format import to_json
from gendiff.gen_diff import gen_diff


def get_format(formater: str) -> str:
    '''Get formater-modul based on the selected format'''
    formats = {'stylish': to_stylish, 'plain': to_plain, 'json': to_json}
    return formats[formater]


def generate_diff(file_path1: str, file_path2: str, formater="stylish") -> str:
    '''
    Return the difference between two input files (json or yml)
    in selected output format
    '''
    dict_1 = parse(file_path1)
    dict_2 = parse(file_path2)
    diff_tree = gen_diff(dict_1, dict_2)
    formater = get_format(formater)
    result = formater(diff_tree)
    return result
