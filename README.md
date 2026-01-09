# Beautiful Numbers

## Contributors

-   Jade Chen, Michael Oyatsi, Jackson Lu, Grigory Artazyan

## Summary

Beautiful Numbers is a small Python package that provides utilities for exploring common numerical properties and representations. The goal of the project is educational: to make it easy to inspect whether numbers have certain mathematical properties or to view them in alternative bases without relying on heavy external dependencies.

## Included Functions

-   `is_prime` Tests whether a given integer is a prime number by checking if it has any divisors other than 1 and itself. Useful for small to moderately sized integers.

-   `binary` Converts a non-negative integer into its binary representation, returned as a string. Useful for understanding base-2 representations and bit-level reasoning.

-   `hexa` Converts a non-negative integer into its hexadecimal representation, returned as a string. Useful for understanding base-16 representations.

-   `fib_seq` Generates the Fibonacci sequence from 1 up to a given positive integer n. The output illustrates the recursive growth pattern of the sequence.

## Contribution to Python Ecosystem

Much of this functionality exists in the Python standard library or in established scientific packages, this package does not aim to replace those tools. Instead, it provides a minimal, self-contained set of functions with explicit logic that is easy to read and reason about.