import json
import yaml


def get_file_format(pathfile):
    file_format = pathfile.split('.')[-1].strip()
    return file_format


def get_data(pathfile):
    result = ''
    with open(pathfile) as file:
        for line in file:
            result += line
    return result


def parse(pathfile):
    data = get_data(pathfile)
    file_format = get_file_format(pathfile)
    result = {}
    if file_format == 'json':
        result = json.loads(data)
    elif file_format in ('yaml', 'yml'):
        result = yaml.safe_load(data)
    return result
