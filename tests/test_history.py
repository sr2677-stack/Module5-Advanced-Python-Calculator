import os
from app.history import HistoryObserver

def test_history_add():
    history = HistoryObserver()
    history.update([2, 3, "add", 5])
    assert len(history.df) == 1

def test_save_load(tmp_path):
    file = tmp_path / "history.csv"

    history = HistoryObserver()
    history.update([1, 2, "add", 3])
    history.save(file)

    new_history = HistoryObserver()
    new_history.load(file)

    assert len(new_history.df) == 1