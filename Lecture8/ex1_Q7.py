# solving common recursion mistakes
def sum_every_other_number(n):
    """Return the sum of every other natural number
    up to n, inclusive.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n <= 0:
        return 0
    else:
        return n + sum_every_other_number(n - 2)

# was originally n == 0, made it so if it was odd numbers n-2 went into
# negatives, making the program go on forever. n <= 0 correction fixed it.
#print(sum_every_other_number(9))

def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    """
    if n < 0:
        print("Non-computable")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
       return fibonacci(n - 1) + fibonacci(n - 2)
# had to change 0 to non computable (goes into negatives.. which don't compute)
# also made hard rule for 1 and 2, as 1 = f(0) - f(-1) == 0, and 2 = f(1) - f(0) (should be 1)
print(fibonacci(11))