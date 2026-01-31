"""
A module that returns numbers as binary representation.

Converts a non-negative integer into its binary representation, returned as a string.
Useful for understanding base-2 representations and bit-level reasoning.
"""


def binary(num):
    """
    >> Covert whole number to binary representation.

    Parameters
    ----------
    num : int
        The number to convert.

    Returns
    -------
    string
        The converted string representation of the number.

    Examples
    --------
    >>> binary(15)
    "1111"

    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    if num < 0:
        raise ValueError("Input must be a non-negative integer")

    if num == 0:
        return "0"

    binary_str = []
    while num > 0:
        bit = num & 1
        num = num >> 1
        binary_str.append(str(bit))

    binary_str.reverse()
    delimiter = ""
    return delimiter.join(binary_str)
