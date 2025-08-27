def bitcount(n):
    count = 0
    n = n & 0xFFFFFFFFFFFFFFFF  # Convert n to 64-bit two's complement representation
    while n:
        n ^= n - 1
        count += 1
    return count