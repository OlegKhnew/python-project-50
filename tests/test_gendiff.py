from gendiff.engine import generate_diff
import pytest


jsonfile1 = "tests/fixtures/file1.json"
jsonfile2 = "tests/fixtures/file2.json"
ymlfile1 = "tests/fixtures/file1.yml"
ymlfile2 = "tests/fixtures/file2.yml"
test_stylish = "tests/fixtures/stylish.txt"
test_plain = "tests/fixtures/plain.txt"
test_json = "tests/fixtures/jsontest.json"


@pytest.mark.parametrize('file1, file2, format, expected',
                         [(jsonfile1, jsonfile2, 'stylish', test_stylish),
                          (ymlfile1, ymlfile2, 'stylish', test_stylish),
                          (jsonfile1, jsonfile2, 'plain', test_plain),
                          (ymlfile1, ymlfile2, 'plain', test_plain),
                          (jsonfile1, jsonfile2, 'json', test_json),
                          (ymlfile1, ymlfile2, 'json', test_json)])
def test_generate_diff(file1, file2, format, expected):
    with open(expected) as file:
        assert generate_diff(file1, file2, format) == file.read().strip()
