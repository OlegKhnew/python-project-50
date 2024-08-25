import json


def to_string(value, depth=0) -> str:
    ''' Transfer value to string '''
    if isinstance(value, dict):
        indent = ' ' * (depth * 4 + 2)
        current_indent = indent + (' ' * 6)
        lines = []
        for key, val in value.items():
            lines.append(f'{current_indent}{key}: {to_string(val, depth + 1)}')
        result = '\n'.join(lines)
        return f"{{\n{result}\n  {indent}}}"
    else:
        return json.dumps(value).replace('"', "")


def to_stylish(data: list, depth=0) -> str:  # noqa: C901
    ''' Transfer data to stylish format '''
    result = '{\n'
    indent = '  '
    for i in range(depth):
        indent += '    '
    for item in data:
        status = item['status']
        key = item['key']
        value = to_string(item.get('value'), depth)
        old_value = to_string(item.get('old_value'), depth)
        new_value = to_string(item.get('new_value'), depth)
        if status == 'node':
            newdata = item['value']
            result += f"{indent}  {key}: {to_stylish(newdata, depth + 1)}\n"
        elif status == 'added':
            result += f"{indent}+ {key}: {value}\n"
        elif status == 'changed':
            result += f"{indent}- {key}: {old_value}\n"
            result += f"{indent}+ {key}: {new_value}\n"
        elif status == 'removed':
            result += f"{indent}- {key}: {value}\n"
        elif status == 'unchanged':
            result += f"{indent}  {key}: {value}\n"
    result += indent[:-2] + "}"
    return result
