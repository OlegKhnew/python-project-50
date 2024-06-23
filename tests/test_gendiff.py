from gendiff.gendiff import generate_diff
from fixtures.testdatas import result


def test_generate_diff(result):
    testfile1 = 'tests/fixtures/testfile1.json'
    testfile2 = 'tests/fixtures/testfile2.json'
    output = generate_diff(testfile1,testfile2)
    assert output == result
