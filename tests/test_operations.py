import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root, OperationFactory

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert Add().execute(a, b) == expected

def test_divide():
    assert Divide().execute(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(5, 0)

def test_factory_valid():
    op = OperationFactory.create("add")
    assert op.execute(2, 2) == 4

def test_factory_invalid():
    with pytest.raises(ValueError):
        OperationFactory.create("invalid")

def test_subtract():
    from app.operations import Subtract
    assert Subtract().execute(10, 3) == 7


def test_multiply():
    from app.operations import Multiply
    assert Multiply().execute(4, 5) == 20


def test_power():
    from app.operations import Power
    assert Power().execute(2, 4) == 16


def test_root():
    from app.operations import Root
    assert round(Root().execute(9, 2), 2) == 3.0        