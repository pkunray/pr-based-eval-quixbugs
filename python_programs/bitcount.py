def bitcount(n):
    count = 0
    while n:
        # Fixed bug: replaced XOR with AND assignment to correctly clear the least significant set bit
        n &= n - 1
        count += 1
    return count
