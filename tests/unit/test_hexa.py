from beautifulnumbers.hexa import hexa
import pytest

def test_hexa_all_same_digit():
    """Test numbers that produce repeated digits."""
    assert hexa(17) == "11"       # 16 + 1
    assert hexa(4369) == "1111"   # repeating 1s

def test_hexa_max_digits():
    """Test numbers that are one less than powers of 16 (all F's)."""
    assert hexa(15) == "F"
    assert hexa(255) == "FF"
    assert hexa(4095) == "FFF"
    assert hexa(65535) == "FFFF"

def test_hexa_spells_words():
    """Test numbers that spell fun words in hex!"""
    assert hexa(48879) == "BEEF"
    assert hexa(51966) == "CAFE"
    assert hexa(57005) == "DEAD"
    assert hexa(64206) == "FACE"
    assert hexa(2989) == "BAD"

def test_hexa_legendary():
    """The famous DEADBEEF."""
    assert hexa(3735928559) == "DEADBEEF"
    
def test_hexa_zero():
    """Test that zero returns '0'."""
    assert hexa(0) == "0"

def test_hexa_boundary_at_sixteen():
    """Test around the 16 boundary."""
    assert hexa(15) == "F"   # last single digit
    assert hexa(16) == "10"  # first two digits
    assert hexa(17) == "11"

def test_binary_negative_raises_error():
    """Test that negative numbers raise ValueError."""
    with pytest.raises(ValueError, match="non-negative integer"):
        hexa(-1)

def test_hexa_non_integer_raises_error():
    """Test that non-integers raise TypeError."""
    with pytest.raises(TypeError, match="must be an integer"):
        hexa(3.14)

    with pytest.raises(TypeError, match="must be an integer"):
        hexa("15")

    with pytest.raises(TypeError, match="must be an integer"):
        hexa([15])

    with pytest.raises(TypeError, match="must be an integer"):
        hexa(None)