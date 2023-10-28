def factorial(n):
    """
    Compute the factorial of a number.

    Args:
    - n (int): The number for which to compute the factorial. Must be a non-negative integer.

    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
