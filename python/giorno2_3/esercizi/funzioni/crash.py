def factorial(n):
    """Calculate the factorial of the given number"""

    if n == 0 or n == 1:  # Caso base per 0 e 1
        return 1
    else:
        return n * factorial(n-1)


assert factorial(5) == 120
assert factorial(0) == 1