import pytest

#Fixture autouse
#autouse is an aurgument and we just sepcify True no need to call(tc_setup) in another file it will automatically calls(tc_setup).
# @pytest.fixture(autouse=True)
# @pytest.fixture()
# def tc_setup():       #setup
#     print("lanuch browser")
#     print("login")
#     print("browse products")
#     yield          #teardown
#     print("logoff")
#     print("close browser")

#Fixture scope
# scope = "session  use of this scope ="session" is when ever we want to execute all testcase and first setup will execute and all test cases and last teardown will execute
# "
# @pytest.fixture(scope="session",autouse=True)
# def tc_setup1():       #setup
#     print("lanuch browser")
#     print("login")
#     print("browse products")
#     yield          #teardown
#     print("logoff")
#     print("close browser")

#o/p:

# collecting ... collected 5 items
#
# test_file1.py::testadd1 lanuch browser
# login
# browse products
# PASSED                                           [ 20%]i am in test_add1
#
# test_file1.py::TestAdd::test_add2 PASSED                                 [ 40%]i am in test_add2
#
# test_file1.py::TestAdd::test_add3 PASSED                                 [ 60%]i am in test_add3
#
# test_file1.py::test_add4 PASSED                                          [ 80%]
# test_file1.py::test_square PASSED                                        [100%]logoff
# close browser


# when we keep function fixture then we get separate testcases get executed with setup and teardown.
#without scope = "function" also it is same as autouse
@pytest.fixture(scope="function",autouse=True)
def tc_setup():       #setup
    print("lanuch browser")
    print("login")
    print("browse products")
    yield          #teardown
    print("logoff")
    print("close browser")



# (base) PS D:\case2> pytest -v -s tests/test_file1.py
# ===================================================================== test session starts =====================================================================
# platform win32 -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- C:\Users\surya\anaconda3\python.exe
# cachedir: .pytest_cache
# rootdir: D:\case2
# plugins: anyio-2.2.0
# collected 5 items
#
# tests/test_file1.py::testadd1 lanuch browser
# login
# browse products
# i am in test_add1
# PASSEDlogoff
# close browser
#
# tests/test_file1.py::TestAdd::test_add2 lanuch browser
# login
# browse products
# i am in test_add2
# PASSEDlogoff
# close browser
#
# tests/test_file1.py::TestAdd::test_add3 lanuch browser
# login
# browse products
# i am in test_add3
# PASSEDlogoff
# close browser
#
# tests/test_file1.py::test_add4 lanuch browser
# login
# browse products
# PASSEDlogoff
# close browser
#
# tests/test_file1.py::test_square lanuch browser
# login
# browse products
# PASSEDlogoff
# close browser






