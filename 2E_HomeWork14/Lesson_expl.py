def is_prime(n: int) -> bool:
    """
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True

    """

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
