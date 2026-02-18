from abc import ABC, abstractmethod
import math


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass  # pragma: no cover

class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        return math.pow(a, 1 / b)


class OperationFactory:
    @staticmethod
    def create(operation_name):
        operations = {
            "add": Add(),
            "sub": Subtract(),
            "mul": Multiply(),
            "div": Divide(),
            "pow": Power(),
            "root": Root(),
        }

        if operation_name not in operations:
            raise ValueError("Invalid operation")

        return operations[operation_name]