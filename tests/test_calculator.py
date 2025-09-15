import pytest
from app.calculator.calculator import calculator

def test_calculator_add(monkeypatch, capsys):
    """Test addition operation."""
    user_inputs = iter(["add 4 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "the result is 9" in captured.out.lower()


def test_calculator_subtract(monkeypatch, capsys):
    """Test subtraction operation."""
    user_inputs = iter(["subtract 10 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "the result is 7" in captured.out.lower()


def test_calculator_multiply(monkeypatch, capsys):
    """Test multiplication operation."""
    user_inputs = iter(["multiply 3 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "the result is 15" in captured.out.lower()


def test_calculator_divide(monkeypatch, capsys):
    """Test division operation."""
    user_inputs = iter(["divide 8 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "the result is 4" in captured.out.lower()


def test_calculator_multiple_operations(monkeypatch, capsys):
    """Test running multiple operations in sequence."""
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
    assert "the result is 3" in captured.out.lower()
    assert "the result is 2" in captured.out.lower()
    assert "the result is 6" in captured.out.lower()
    assert "the result is 4" in captured.out.lower()

def test_calculator_invalid_operation(monkeypatch, capsys):
    """Test that invalid operation input triggers 'Invalid input' message."""
    user_inputs = iter(["foobar 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "invalid input" in captured.out.lower()


def test_calculator_invalid_numbers(monkeypatch, capsys):
    """Test that non-numeric inputs trigger 'not a valid number' message."""
    user_inputs = iter(["add a b", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "not a valid number" in captured.out.lower()


def test_calculator_divide_by_zero(monkeypatch, capsys):
    """Test that division by zero triggers the appropriate message."""
    user_inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "cannot divide by zero" in captured.out.lower()


def test_calculator_exit_only(monkeypatch, capsys):
    """Test that entering 'exit' immediately prints the goodbye message."""
    user_inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "thank you for using the calculator" in captured.out.lower()


def test_calculator_whitespace_and_case(monkeypatch, capsys):
    """Test that calculator handles extra spaces and uppercase commands."""
    user_inputs = iter(["  ADD   3   4  ", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    calculator()
    captured = capsys.readouterr()
    assert "the result is 7" in captured.out.lower()
