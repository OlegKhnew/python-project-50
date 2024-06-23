import pytest
import json


@pytest.fixture
def result():
    return '{\n  atest: input1\n- ctest3: 100.200.00.00\n+ ctest3: 100.200.11.22\n- dtest: 1\n+ etest: 2\n- test4: false\n+ test4: true\n}'


#@pytest.fixture
#def testfile1('testfile1.json'):
#    with open('testfile1.json', 'r') as file_1: 
#	testcoll1 = file_1.read)
#    return testcoll1


#@pytest.fixture
#def testfile2('testfile2.json'):
#    with open('testfile2.json', 'r') as file_2:
#	testcoll2 = file_2.read()
#    return testcoll2


#@pytest.fixture
#def testfile1('testfile1.json'):
#    return 'testfile1.json'

#@pytest.fixture
#def testfile2('testfile2.json'):
#    return 'testfile2.json'
