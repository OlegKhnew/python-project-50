import json


def format_to_dict(data: list) -> dict:
    ''' Transform list to dict '''
    result = {}
    for item in data:
        status = item['status']
        key = item['key']
        if status == 'node':
            newdata = item['value']
            result[key] = format_to_dict(newdata)
        elif status == 'changed':
            result[key] = {'status': item['status'],
                           'old_value': item['old_value'],
                           'new_value': item['new_value']}
        else:
            result[key] = {'status': item['status'],
                           'value': item['value']}
    return result


def to_json(data: list):
    ''' Transform data to json-format view '''
    result = format_to_dict(data)
    return json.dumps(result, indent=2)
