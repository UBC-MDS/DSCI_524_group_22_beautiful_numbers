# MIT License
#
# Copyright (c) 2026 Jade Chen; Grigory Artazyan; Jackson Lu; Michael Oyatsi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Beautiful Numbers - A collection of number theory and conversion utilities.

This package provides functions for:
- Converting numbers to binary and hexadecimal representations
- Generating Fibonacci sequences
- Finding prime numbers

Functions
---------
binary(num)
    Convert a non-negative integer to binary representation.
hexa(number)
    Convert a non-negative integer to hexadecimal representation.
fib_seq(n)
    Generate the Fibonacci sequence of length n.
prime_list(n)
    Generate a list of all prime numbers up to and including n.
"""

from beautifulnumbers.binary import binary
from beautifulnumbers.fib_seq import fib_seq
from beautifulnumbers.hexa import hexa
from beautifulnumbers.prime_list import prime_list

__all__ = ["binary", "fib_seq", "hexa", "prime_list"]
