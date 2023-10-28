import pytest
import sys
sys.path.insert(0,"D:\case2\codes") #when files r in different location
from common import get_common,uniq,sub
# from conftest import tc_setup
#(no need to import when we give file name as conftest.py only) it will automatically call we we give function name.


def test_u1():
    out = uniq([11,22,33,33,33,3,22,22,11])
    if out == [11,22,33,3]:
        assert True
    else:
        assert False

# @pytest.mark.skip(reason="dont run because it will fail")
def test_common1():
    out = get_common([10,20,30],[20,90,10])
    if out == [10,20]:
        assert True
    else:
        assert False

# @pytest.mark.slow
def test_sub1():
    out = sub(10,4)
    if out ==40:
        assert True
    else:
        assert False





