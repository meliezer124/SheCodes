# writing a recursive function that computes sum of all integers in list

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)


print(sum(3))

print(sum(6))

print(sum(10))