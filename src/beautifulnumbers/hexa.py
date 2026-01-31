"""
Utilities for base conversion.

This module provides a function for converting non-negative integers
from decimal (base-10) representation into hexadecimal (base-16),
returning the result as an uppercase string.
"""


def hexa(number):
    """
    >> Converts a decimal (base-10) number into hexadecimal (base-16).

    Parameters
    ----------
    number : int
        The decimal number to convert.

    Returns
    -------
    str
        The hexadecimal representation of the number.

    Examples
    --------
    >>> hexa(10)
    'A'
    >>> hexa(255)
    'FF'
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number < 0:
        raise ValueError("Input must be a non-negative integer")

    if number == 0:
        return '0'
    
    hex_chars = '0123456789ABCDEF'
    result = ''
    
    while number > 0:
        remainder = number % 16
        result = hex_chars[remainder] + result
        number = number // 16
    
    return result
