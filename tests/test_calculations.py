from app.calculation import Calculator

def test_calculate_add():
    calc = Calculator()
    result = calc.calculate(2, 3, "add")
    assert result == 5

def test_history_updated():
    calc = Calculator()
    calc.calculate(2, 3, "add")
    assert len(calc.history_observer.df) == 1
def test_undo_without_history():
    from app.calculation import Calculator
    calc = Calculator()
    assert calc.undo() is None


def test_redo_without_history():
    from app.calculation import Calculator
    calc = Calculator()
    assert calc.redo() is None    