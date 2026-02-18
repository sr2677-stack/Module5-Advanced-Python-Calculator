from app.operations import OperationFactory
from app.history import HistoryObserver
from app.calculator_memento import Caretaker

class Calculator:
    def __init__(self):
        self.observers = []
        self.history_observer = HistoryObserver()
        self.caretaker = Caretaker()
        self.current_state = None

        self.attach(self.history_observer)

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)

    def calculate(self, a, b, operation_name):
        operation = OperationFactory.create(operation_name)
        result = operation.execute(a, b)

        data = [a, b, operation_name, result]
        self.notify(data)

        self.current_state = result
        self.caretaker.save(result)

        return result

    def undo(self):
        return self.caretaker.undo()

    def redo(self):
        return self.caretaker.redo()