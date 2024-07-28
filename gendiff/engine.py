#!/usr/bin/env python3

from gendiff.parser import parse
from gendiff.stylish import to_stylish
from gendiff.get_diff_tree import get_difftree


def get_format(formater):
    formats = {'stylish': to_stylish}
    return formats[formater]


def generate_diff(file_path1, file_path2, formater="stylish"):
    dict_1 = parse(file_path1)
    dict_2 = parse(file_path2)
    diff_tree = get_difftree(dict_1, dict_2)
    formater = get_format(formater)
    result = formater(diff_tree)
    return result
