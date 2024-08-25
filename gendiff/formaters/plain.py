
def to_string(value: str) -> str:
    ''' Transform value to string and node-values to "complex value" '''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, int):
        return value
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def to_plain(tree: list, path='') -> str:  # noqa: C901
    ''' Transform data to plain format'''
    result = []
    for item in tree:
        status = item['status']
        value = to_string(item.get('value'))
        old_value = to_string(item.get('old_value'))
        new_value = to_string(item.get('new_value'))
        curr_path = f'{path}{item.get("key")}'
        if status == 'node':
            addtree = item["value"]
            lines = to_plain(addtree, f"{curr_path}.")
            result.append(lines)
        elif status == 'added':
            result.append(f"Property '{curr_path}' was added "
                          f"with value: {value}")
        elif status == 'removed':
            result.append(f"Property '{curr_path}' was removed")
        elif status == 'changed':
            result.append(f"Property '{curr_path}' was updated. "
                          f"From {old_value} to {new_value}")
        elif status == 'unchanged':
            pass
    return '\n'.join(result)
