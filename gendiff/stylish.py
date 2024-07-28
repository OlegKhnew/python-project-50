import json


def newvalue(val):
    if isinstance(val, dict):
        return val
    else:
        return json.dumps(val).replace('"', "")


def form_dict(val, depth):
    if not isinstance(val, dict):
        return val
    result = ["{"]
    for key, value in val.items():
        result.append(f"\n{'  '*(depth)}  "
                      f"{key}: {form_dict(value, depth+2)}")
    result.append(f"\n{'  '*(depth-1)}}}")
    return ''.join(result)


def get_strings(newtree, depth=1, result=None):
    indent = depth * '  '
    if result is None:
        result = []
    for key, value in newtree.items():
        status = value['status']
        if status == 'node':
            result.append(f"{indent}  {key}: {{")
            result.append(get_strings(value['value'], depth + 2, result))
            result.append(f"{indent}  }}")
        elif status == 'added':
            result.append(f"{indent}+ {key}: "
                          f"{form_dict(newvalue(value['value']), depth+2)}")
        elif status == 'removed':
            result.append(f"{indent}- {key}: "
                          f"{form_dict(newvalue(value['value']), depth+2)}")
        elif status == 'unchanged':
            result.append(f"{indent}  {key}: "
                          f"{form_dict(newvalue(value['value']), depth+2)}")
        elif status == 'changed':
            result.append(f"{indent}- {key}: "
                          f"{form_dict(newvalue(value['old_value']), depth+2)}")
            result.append(f"{indent}+ {key}: "
                          f"{form_dict(newvalue(value['new_value']), depth+2)}")
    return result


def to_stylish(newtree):
    result = get_strings(newtree, result=[])
    result.insert(0, '{')
    result.append('}\n')
    output = []
    for item in result:
        if not isinstance(item, list):
            output.append(item)
    output_string = '\n'.join(output)
    return output_string
