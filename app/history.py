import pandas as pd

class Observer:
    def update(self, data):
        pass  # pragma: no cover

class HistoryObserver(Observer):
    def __init__(self):
        self.df = pd.DataFrame(columns=["a", "b", "operation", "result"])

    def update(self, data):
        self.df.loc[len(self.df)] = data

    def save(self, filename):
        self.df.to_csv(filename, index=False)

    def load(self, filename):
        self.df = pd.read_csv(filename)