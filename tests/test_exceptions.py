import pytest
from app.exceptions import InvalidInputError

def test_invalid_input_exception():
    with pytest.raises(InvalidInputError):
        raise InvalidInputError("Invalid")