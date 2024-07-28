
def get_difftree(dict_1, dict_2):
    diff = {}
    for key1 in dict_1.keys():
        if key1 not in dict_2.keys():
            diff[key1] = {'status': 'removed', 'value': dict_1[key1]}
        elif isinstance(dict_1[key1], dict) \
                and isinstance(dict_2[key1], dict):
            diff[key1] = {'status': 'node',
                          'value': get_difftree(dict_1[key1],
                                                dict_2[key1])}
        elif dict_1[key1] == dict_2[key1]:
            diff[key1] = {'status': 'unchanged',
                          'value': dict_1[key1]}
        else:
            diff[key1] = {'status': 'changed',
                          'old_value': dict_1[key1],
                          'new_value': dict_2[key1]}
    for key2 in dict_2.keys():
        if key2 not in dict_1.keys():
            diff[key2] = {'status': 'added', 'value': dict_2[key2]}

    return dict(sorted(diff.items()))
