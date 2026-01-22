from beautifulnumbers.fib_seq import fib_seq
import pytest

# note: used chatgpt to identify missing edge cases (caught the missing base cases test)

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

def test_fib_seq_large_n_last_value():
    """Check last value for a larger n to ensure scaling and correctness"""
    # fib_seq is 1-indexed with [1, 1, 2, ...], so n=30 ends with F30 = 832040
    assert fib_seq(30)[-1] == 832040


def test_fib_seq_monotonic_non_decreasing():
    """Check sequence is non-decreasing for n >= 2"""
    result = fib_seq(25)
    assert all(result[i] >= result[i - 1] for i in range(1, len(result)))