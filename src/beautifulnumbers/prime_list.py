def prime_list(n):
    """
    Generate a list of all prime numbers up to and including n.
    
    This function uses the Sieve of Eratosthenes algorithm to efficiently
    find all prime numbers in the range [2, n].
    
    Parameters
    ----------
    n : int
        The upper bound (inclusive) for finding prime numbers.
        Must be a non-negative integer.
    
    Returns
    -------
    list of int
        A list containing all prime numbers from 2 up to and including n,
        in ascending order. Returns an empty list if n < 2.
    
    Raises
    ------
    Exception
        If n is not an integer.
    Exception
        If n is a negative integer.
    
    Examples
    --------
    >>> prime_list(10)
    [2, 3, 5, 7]
    
    >>> prime_list(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    
    >>> prime_list(2)
    [2]
    
    >>> prime_list(1)
    []
    
    >>> prime_list(0)
    []
    
    Notes
    -----
    The Sieve of Eratosthenes works by iteratively marking the multiples of 
    each prime number starting from 2. The algorithm has O(n log log n) time 
    complexity and O(n) space complexity, making it efficient for finding all 
    primes up to a given limit.
    
    This implementation is optimized by only checking multiples starting from
    the square of each prime, and only iterating up to the square root of n
    for the sieving process.
    """
    
    
    prime_list = []
    
    # Exception handling for invalid inputs
    if type(n) is not int or isinstance(n, bool):
        raise Exception("The input must be an integer")
    
    if n < 0:
        raise Exception("The input must be a positive integer") 
    
    # Edge cases for 0 and 1   
    if n == 0:
        return []
    
    elif n == 1:
        return []
    

    else:
        numbers = [True for idx in range(n + 1)] 
        
        numbers[0] = False
        numbers[1] = False
        
        for num in range (2, round((n) ** 0.5) + 1):
            if numbers[num]:
                increment = 0
                j = num ** 2 + increment * num
                while j <= n:
                    numbers[j] = False
                    increment += 1
                    j = num ** 2 + increment * num
        
        for prime in range(n + 1):
            if numbers[prime]:
                prime_list.append(prime)
    return prime_list 