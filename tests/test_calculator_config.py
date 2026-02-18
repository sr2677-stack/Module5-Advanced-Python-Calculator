import os
import pytest
from app.calculator_config import Config

def test_default_history_file():
    assert Config.HISTORY_FILE is not None

def test_invalid_config(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "")
    with pytest.raises(ValueError):
        Config.validate()