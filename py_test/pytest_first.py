# pytest pytest_first.py -m "focus"
# pytest pytest_first.py -m "not focus"


import pytest


# def func(x):
#     return x+5
#
# def test_method1():
#     assert func(3)==8
#
# @pytest.mark.xfail
# def test_method2():
#     assert func(3)==9
#
# @pytest.mark.focus
# def test_method3():
#     assert func(5)==12

# fixture runs first before test_functions()
@pytest.fixture
def func():
    x = 10
    y = 20
    return [x, y]


def test_first(func):
    assert func[0] == 10


def test_sec(func):
    assert func[1] == 10


# using focus to only run the parameterized marker
@pytest.mark.focus
@pytest.mark.parametrize("a,b", [(10, 20), (5, 5)])
def test_add(a, b):
    assert 10 + a == b

# @pytest.mark.custom
# def test_multiply():
#     assert 5 * 5 == 100
#
#
# @pytest.mark.focus
# def test_adding():
#     assert 5 + 5 == 10
