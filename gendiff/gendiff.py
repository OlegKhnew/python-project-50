#!/usr/bin/env python3

import json


def get_diff_dict(dict_1, dict_2):
    diff = {}
    items1, items2 = dict_1.keys(), dict_2.keys()
    # if you need sort your result in abc-order - activate next step.
    items = sorted(set(items1) | set(items2))
    for item in items:
        if item in items1 and item not in items2:
            diff[item] = {'status': 'removed', 'value': dict_1[item]}
        if item in items1 and item in items2 and dict_1[item] == dict_2[item]:
            diff[item] = {'status': 'unchanged', 'value': dict_1[item]}
        if item in items1 and item in items2 and dict_1[item] != dict_2[item]:
            diff[item] = {'status': 'changed', 'old_value': dict_1[item],
                          'new_value': dict_2[item]}
        if item not in items1 and item in items2:
            diff[item] = {'status': 'added', 'value': dict_2[item]}

    return diff


def get_output(diff):
    output = "{\n"
    for k, v in diff.items():
        if v['status'] == 'changed':
            old_value = str(v['old_value'])
            new_value = str(v['new_value'])
            output += (f'- {k}: {old_value}\n')
            output += (f'+ {k}: {new_value}\n')
        else:
            status = v['status'].replace('unchanged', ' ')\
                                .replace('added', '+').replace('removed', '-')
            value = str(v['value'])
            output += (f'{status} {k}: {value}\n')
    output += '}'

    output = output.replace('False', 'false').replace('True', 'true')

    return output


def generate_diff(file_path1, file_path2):
    dict_1 = json.load(open(file_path1))
    dict_2 = json.load(open(file_path2))
    diff_dict = get_diff_dict(dict_1, dict_2)
    result = get_output(diff_dict)
    return result
