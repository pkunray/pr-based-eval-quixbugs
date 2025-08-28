def bitcount(n):
    n = abs(n)  # Convert negative numbers to positive
    count = 0
    while n:
        n ^= n - 1
        count += 1
    return count
