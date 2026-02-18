import re
from typing import Union, List, Tuple
from decimal import Decimal, InvalidOperation
from .exceptions import InvalidInputError

def validate_number(value: str) -> Union[int, float, Decimal]:
    """
    Validate and convert a string to a number (int, float, or Decimal).
    
    Args:
        value: The string value to validate and convert
        
    Returns:
        The converted number (int, float, or Decimal)
        
    Raises:
        InvalidInputError: If the value cannot be converted to a valid number
    """
    if not value.strip():
        raise InvalidInputError("Empty input")
    
    try:
        # Try to convert to int first
        return int(value)
    except ValueError:
        try:
            # If not an int, try float
            float_val = float(value)
            # If it's a float but has no decimal part, return as int
            if float_val.is_integer():
                return int(float_val)
            return float_val
        except (ValueError, TypeError):
            # If all else fails, try Decimal
            try:
                return Decimal(value)
            except (InvalidOperation, TypeError) as e:
                raise InvalidInputError(f"Invalid number: {value}") from e

def validate_operation(operation: str) -> str:
    """
    Validate that the operation is one of the supported operations.
    
    Args:
        operation: The operation to validate
        
    Returns:
        The validated operation in lowercase
        
    Raises:
        InvalidInputError: If the operation is not supported
    """
    operation = operation.strip().lower()
    supported_ops = ['+', '-', '*', '/', '**', '//', '%']
    
    if operation not in supported_ops:
        raise InvalidInputError(
            f"Unsupported operation: {operation}. "
            f"Supported operations are: {', '.join(supported_ops)}"
        )
    return operation

def parse_expression(expression: str) -> Tuple[Union[int, float, Decimal], str, Union[int, float, Decimal]]:
    """
    Parse a simple mathematical expression into its components.
    
    Args:
        expression: The expression to parse (e.g., "2 + 2")
        
    Returns:
        A tuple of (first_number, operation, second_number)
        
    Raises:
        InvalidInputError: If the expression cannot be parsed
    """
    # Remove all whitespace
    expr = re.sub(r'\s+', '', expression)
    
    # Match numbers (including decimals and negative numbers) and operators
    pattern = r'^([-+]?\d*\.?\d+)([+\-*/%]|\*\*|//)([-+]?\d*\.?\d+)$'
    match = re.match(pattern, expr)
    
    if not match:
        raise InvalidInputError(
            "Invalid expression format. Expected format: 'number operator number' (e.g., '2 + 2' or '3.14 * 2')"
        )
    
    num1_str, op, num2_str = match.groups()
    
    try:
        num1 = validate_number(num1_str)
        num2 = validate_number(num2_str)
        return num1, op, num2
    except InvalidInputError as e:
        raise InvalidInputError(f"Invalid number in expression: {e}") from e