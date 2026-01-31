"""
Utilities for generating Fibonacci sequences.

This module provides a function for constructing the Fibonacci sequence
up to a specified length using a bottom-up iterative approach, with
explicit input validation and clear base case handling.
"""


def fib_seq(n):
    """
    >> Generates the Fibonacci sequence from 1 up to a given positive integer n.

    Parameters
    ----------
    n : integer
        The length of the Fibonacci sequence.

    Returns
    -------
    list of int
        The Fibonacci sequence of length n.

    Examples
    --------
    >>> fib_seq(1)
    [1]
    >>> fib_seq(3)
    [1,1,2]

    """
    # checks inputs & exception handling
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    # base case
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    # bottom-up approach (note: referenced DSCI 512 notes)
    seq = [1, 1]
    for _ in range(2, n): # repeat this block n - 2 times (note: _ means ignored)
        seq.append(seq[-1] + seq[-2])

    return seq