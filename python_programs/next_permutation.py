def next_permutation(perm):
    # Handle edge cases
    if len(perm) <= 1:
        return perm

    # Find the first index 'i' such that perm[i] < perm[i + 1]
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            # Find the first index 'j' such that perm[j] > perm[i]
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:
                    # Swap elements at i and j
                    perm[i], perm[j] = perm[j], perm[i]
                    # Reverse the sequence from i + 1 to end
                    perm[i + 1:] = reversed(perm[i + 1:])
                    return perm
    # If no such index exists, the permutation is the last permutation
    perm.reverse()
    return perm


"""
Next Permutation
next-perm


Input:
    perm: A list of unique ints

Precondition:
    perm is not sorted in reverse order

Output:
    The lexicographically next permutation of the elements of perm

Example:
    >>> next_permutation([3, 2, 4, 1])
    [3, 4, 1, 2]
"""
