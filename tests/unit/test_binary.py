from src.beautifulnumbers.binary import binary
import pytest


def test_binary_basic():
    assert binary(15) == "1111"


def test_binary_zero():
    assert binary(0) == "0"


def test_binary_one():
    """Test smallest positive number."""
    assert binary(1) == "1"


def test_binary_power_of_two():
    """Test powers of 2 have a single 1 bit."""
    assert binary(2) == "10"
    assert binary(4) == "100"
    assert binary(8) == "1000"
    assert binary(16) == "10000"
    assert binary(256) == "100000000"


def test_binary_negative_raises_error():
    """Test that negative numbers raise ValueError."""
    with pytest.raises(ValueError, match="non-negative integer"):
        binary(-1)


def test_binary_non_integer_raises_error():
    """Test that non-integers raise TypeError."""
    with pytest.raises(TypeError, match="must be an integer"):
        binary(3.14)

    with pytest.raises(TypeError, match="must be an integer"):
        binary("15")

    with pytest.raises(TypeError, match="must be an integer"):
        binary([15])

    with pytest.raises(TypeError, match="must be an integer"):
        binary(None)


def test_binary_very_large_number():
    """Test with a very large number."""
    # 2^20 = 1048576
    result = binary(1048576)
    assert result == "100000000000000000000"
    assert len(result) == 21
