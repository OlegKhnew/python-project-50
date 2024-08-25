
def gen_diff(dict_1: dict, dict_2: dict) -> list:
    '''
    Function creates a difference representation
    in a tree-data structure.
    '''
    keys = dict_1.keys() | dict_2.keys()
    diff = []
    for key in sorted(keys):
        value_1 = dict_1.get(key)
        value_2 = dict_2.get(key)
        if key not in dict_1:
            diff.append({'key': key, 'status': 'added', 'value': value_2})
        elif key not in dict_2:
            diff.append({'key': key, 'status': 'removed', 'value': value_1})
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            diff.append({'key': key, 'status': 'node',
                         'value': gen_diff(dict_1[key], dict_2[key])})
        elif dict_1[key] == dict_2[key]:
            diff.append({'key': key, 'status': 'unchanged', 'value': value_1})
        else:
            diff.append({'key': key, 'status': 'changed', 'old_value': value_1,
                         'new_value': value_2})
    return diff
