from beautifulnumbers.fib_seq import fib_seq
import pytest

def test_fib_seq_invalid_type():
    """Check if raises a TypeError when the input is not an integer"""
    with pytest.raises(TypeError):
        fib_seq(3.5)

def test_fib_seq_invalid_input():
    """Check if raises a ValueError when the input is zero or negative"""
    with pytest.raises(ValueError):
        fib_seq(0)
    with pytest.raises(ValueError):
        fib_seq(-4)

def test_fib_seq_base_cases():
    """Check if correct Fibonacci sequences for the smallest valid inputs"""
    assert fib_seq(1) == [1]
    assert fib_seq(2) == [1, 1]

def test_fib_seq_length():
    """Check if returned Fibonacci sequence's length matches the input n"""
    n = 10
    result = fib_seq(n)
    # sequence length should match n
    assert len(result) == n


def test_fib_seq_correct_content():
    """Check if the content of Fibonacci sequence is correct"""
    result = fib_seq(7)
    # each element after the first two should be the sum of the previous two
    for i in range(2, len(result)):
        assert result[i] == result[i - 1] + result[i - 2]