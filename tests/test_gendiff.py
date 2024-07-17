from gendiff.gendiff import generate_diff
import pytest



jsonfile1 = "tests/fixtures/file1.json"
jsonfile2 = "tests/fixtures/file2.json"
ymlfile1 = "tests/fixtures/file1.yml"
ymlfile2 = "tests/fixtures/file2.yml"
testresult = "tests/fixtures/testresult.txt"


@pytest.mark.parametrize('file1, file2, result',
                         [(jsonfile1, jsonfile2, testresult),
                          (ymlfile1, ymlfile2, testresult)])


def test_generate_diff(file1, file2, result):
    with open (result) as file:
        assert generate_diff(file1, file2) == file.read()
