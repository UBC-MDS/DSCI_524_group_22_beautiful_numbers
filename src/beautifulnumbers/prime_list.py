def isprime(n):
    """
    Return a boolean value for whether a number is a prime number. 
    
    Parameters:
    -----------
    n : integer
    
    Returns:
    --------
    Boolean 
        A boolean value depending on whether the number is a prime number or not. 
        
    Examples: 
    ---------
    >>> isprime(3)
    True
    >>> isprime(6)
    False
    """
    
    if n == 0:
        return False
    
    if n == 1:
        return False
    
    else:
   
        numbers = [True for idx in range(n + 1)] 
        
        numbers[0] = False
        numbers[1] = False
        
        for num in range (2, round((n+1) ** 0.5)):
            if numbers[num] == True:
                increment = 0
                j = num ** 2 + increment * num
                while j <= n:
                    numbers[j] = False
                    increment += 1
                    j = num ** 2 + increment * num
                
        return numbers[n]             

def prime_list(limit):
    
    if type(limit) is not int:
        raise Exception("The input must be an integer")
    
    if limit < 0:
        raise Exception("The input must be a positive integer")    
    prime_list = []
    for num in range (0, limit + 1):
        if isprime(num):
            primelist.append(num)
            
    return prime_list