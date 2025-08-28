def bitcount(n):
    n = abs(n)  # Use the absolute value of n to handle negative numbers
    count = 0
    while n:
        n ^= n - 1
        count += 1
    return count
