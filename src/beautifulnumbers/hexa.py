def hexa(number):
    """
    Converts a decimal (base-10) number into hexadecimal (base-16).

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
    >>> convert_to_hex(10)
    'A'
    >>> convert_to_hex(255)
    'FF'
    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    if num < 0:
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
