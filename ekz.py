def arithmetic_sum(n):
    if n <= 0:
        raise ValueError("Incorrect number, must be > 0")
    total = 1
    value = 3
    for i in range(n-1):
        total = total + value
    return total