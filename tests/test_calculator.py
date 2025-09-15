import pytest
from app.calculator.calculator import calculator

def test_calculator_add(monkeypatch, capsys):
    # Simulate user typing "add 4 5" then "exit"
    user_inputs = iter(["add 4 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "The result is 9" in captured.out

def test_calculator_subtract(monkeypatch, capsys):
    user_inputs = iter(["subtract 10 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "The result is 7" in captured.out

def test_calculator_multiply(monkeypatch, capsys):
    user_inputs = iter(["multiply 3 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "The result is 15" in captured.out

def test_calculator_divide(monkeypatch, capsys):
    user_inputs = iter(["divide 8 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "The result is 4" in captured.out

def test_calculator_divide_by_zero(monkeypatch, capsys):
    user_inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "cannot divide by zero" in captured.out.lower()

def test_calculator_invalid_number(monkeypatch, capsys):
    user_inputs = iter(["add a b", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "not a valid number" in captured.out.lower()

def test_calculator_invalid_operation(monkeypatch, capsys):
    user_inputs = iter(["foo 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "invalid input" in captured.out.lower()

def test_calculator_multiple_operations(monkeypatch, capsys):
    # Simulate multiple operations in sequence
    user_inputs = iter([
        "add 1 2",
        "subtract 5 3",
        "multiply 2 3",
        "divide 8 2",
        "exit"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    calculator()
    
    captured = capsys.readouterr()
    assert "The result is 3" in captured.out
    assert "The result is 2" in captured.out
    assert "The result is 6" in captured.out
    assert "The result is 4" in captured.out
