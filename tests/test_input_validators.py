import pytest
from decimal import Decimal

from app.input_validators import (
    validate_number,
    validate_operation,
    parse_expression
)
from app.exceptions import InvalidInputError


# ==================================================
# validate_number Tests
# ==================================================

def test_validate_number_integer():
    assert validate_number("10") == 10


def test_validate_number_float():
    assert validate_number("10.5") == 10.5


def test_validate_number_float_becomes_int():
    # Covers float_val.is_integer() branch
    assert validate_number("10.0") == 10


def test_validate_number_negative():
    assert validate_number("-5") == -5


def test_validate_number_empty():
    # Covers line: if not value.strip()
    with pytest.raises(InvalidInputError):
        validate_number("   ")


def test_validate_number_invalid_string():
    # Covers final InvalidInputError branch
    with pytest.raises(InvalidInputError):
        validate_number("abc")


def test_validate_number_decimal_branch():
    # Forces Decimal fallback branch
    result = validate_number("0.0000000000000000001")
    assert isinstance(result, float) or isinstance(result, Decimal)


# ==================================================
# validate_operation Tests
# ==================================================

def test_validate_operation_valid():
    assert validate_operation("+") == "+"
    assert validate_operation(" * ") == "*"


def test_validate_operation_invalid():
    with pytest.raises(InvalidInputError):
        validate_operation("invalid")


# ==================================================
# parse_expression Tests
# ==================================================

def test_parse_expression_valid():
    num1, op, num2 = parse_expression("2 + 2")
    assert num1 == 2
    assert op == "+"
    assert num2 == 2


def test_parse_expression_float():
    num1, op, num2 = parse_expression("3.5 * 2")
    assert num1 == 3.5
    assert op == "*"
    assert num2 == 2


def test_parse_expression_invalid_format():
    # Covers regex non-match branch
    with pytest.raises(InvalidInputError):
        parse_expression("invalid expression")


def test_parse_expression_invalid_number_nested(monkeypatch):
    """
    Forces nested InvalidInputError branch:
    lines 94–95 in input_validators.py
    """
    from app import input_validators

    def fake_validate_number(value):
        raise InvalidInputError("forced error")

    monkeypatch.setattr(input_validators, "validate_number", fake_validate_number)

    with pytest.raises(InvalidInputError):
        parse_expression("2 + 2")