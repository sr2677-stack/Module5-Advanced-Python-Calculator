class CalculatorError(Exception):
    """Base exception for calculator-related errors"""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is attempted"""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted"""
    pass

class InvalidInputError(CalculatorError):
    """Raised when invalid input is provided"""
    pass

class HistoryError(CalculatorError):
    """Raised for errors related to calculation history"""
    pass
