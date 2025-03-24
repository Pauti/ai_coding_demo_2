def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    fib_sequence = [0, 1]
    if n <= 1:
        return fib_sequence[n]

    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        print(fib_sequence[i])

    return fib_sequence[n]


def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Example usage
fibonacci(10)
print(factorial(5))
