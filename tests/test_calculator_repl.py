import builtins
from app.calculator_repl import run


def test_help_command(monkeypatch):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    run()


def test_invalid_command(monkeypatch):
    inputs = iter(["invalid input", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    run()


def test_valid_calculation(monkeypatch):
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    run()

def test_repl_triggers_exception(monkeypatch):
    # Force division by zero to hit exception block
    inputs = iter(["div 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from app.calculator_repl import run
    run()    

def test_repl_help_command(monkeypatch):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from app.calculator_repl import run
    run()