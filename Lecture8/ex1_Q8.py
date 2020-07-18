ZERO = 0
ONE = 1
TWO = 2
THREE = 3


def hailstone(n, count=1):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    #>>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    #>>> a
    7
    """
    if n == ONE:
        return count
    elif n % TWO == ZERO:
        n = n / TWO
        return hailstone(n, count + ONE)
    else:
        n = (n * THREE) + ONE
        return hailstone(n, count + ONE)


print(hailstone(10))


