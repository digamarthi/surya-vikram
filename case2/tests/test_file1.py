import pytest
import sys
sys.path.insert(0,r"D:\case2\codes")
from common import add
from conftest import tc_setup


# @pytest.fixture()
# def setup():       #setup preconditions
#     print("lanuch browser")
#     print("login")
#     print("browse products")
#     yield          #teardown
#     print("logoff")
#     print("close browser")

#class Testadd:
    # @pytest.fixture(test_file1="class",autouse=True)
    # def myfixture(self):
    #     print("my fixture is called")

#test case name should be start with test* (_)is not manditory (def testadd1())
#when we give testcase file as file1.py and file2.py test cases will execute.
#ex:pytest -v tests/file2.py tests/file1.py we can get both outputs from both files at a time
#if we want to execute all files at a time in tests folder keep file names as test_abc.py (test_  should be must and give any name as abc.py -- test_abc.py)
#ex: pytest -v tests (all files with test_ will execute)

def testadd1():                 #pytest -v -s tests/test_file1.py
    out = add(4,8)
    if out == 12:
        assert True             # assert : to decide the result we have to use assert only
    else:
        assert False
    print("i am in test_add1")

#test suite means collection of test cases:: for one function(scenario) we can write more testcases
#grouping: keeping in testcases in group like adding one group,fast testcases in one group,slow test cases in another group

#pytest -v tests/test_file1.py::TestAdd
class TestAdd:   # Test* (T should be capital and we can add any name after Test)
    def test_add2(self):
        out = add(4,'M')
        if out == None:
            assert True,"succesfully added"
        else:
            assert False
        print("i am in test_add2")

    def test_add3(self):
        out = add(4,15)
        if out == 16:
            assert True
        else:
            assert False,'my mistake'
        print("i am in test_add3")

@pytest.mark.slow
def test_add4():
    out = add(5,8)
    if out == 13:
        assert True
    else:
        assert False


def test_square():
    num = 7
    assert num*num == 49
    