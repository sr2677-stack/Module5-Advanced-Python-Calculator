from app.calculator_memento import Caretaker

def test_undo_redo():
    caretaker = Caretaker()
    caretaker.save(10)
    assert caretaker.undo() == 10
    assert caretaker.redo() == 10

def test_empty_undo():
    caretaker = Caretaker()
    assert caretaker.undo() is None

def test_redo_when_empty():
    from app.calculator_memento import Caretaker

    caretaker = Caretaker()

    # redo without any prior save
    assert caretaker.redo() is None    