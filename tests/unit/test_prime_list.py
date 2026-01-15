from beautifulnumbers.prime_list import prime_list
import pytest

def test_prime_list_output_type():
    """Confirm that the object returned by the function is a list"""
    assert type(prime_list(12)) is list
    
def test_prime_list_int_error():
    """Assert inputing a value other than an integer will raise an error"""
    with pytest.raises(Exception, match="The input must be an integer"):
        prime_list(6.0)
    with pytest.raises(Exception, match="The input must be an integer"):
        prime_list([6.0])
    with pytest.raises(Exception, match="The input must be an integer"):
        prime_list("6")

def test_prime_list_negative_error():
    """Confirm that inputting a negative number will raise an error"""
    with pytest.raises(Exception, match="The input must be a positive integer"):
        prime_list(-8)

def test_prime_list_ten():
    """Confirm that the output of prime_list(10) is [2, 3, 5, 7]"""
    assert prime_list(10) == [2, 3, 5, 7]
    
def test_prime_list_one():
    """Confirm that the output of prime_list(1) is an empty string"""
    assert prime_list(1) == []
    
def test_prime_list_seven():
    """Confirm that when a prime number is used as the input, it is included in the output"""
    assert prime_list(7)[-1] == 7 
    
def test_boolean_input(self):
    """Test that boolean input raises exception (tricky case!)"""

    with pytest.raises(Exception, match="The input must be an integer"):
        prime_list(True)