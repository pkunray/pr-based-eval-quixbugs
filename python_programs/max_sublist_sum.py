def max_sublist_sum(arr):
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        max_ending_here = max_ending_here + x
        if max_ending_here < 0:
            max_ending_here = 0
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

"""
Find the maximum subarray sum, allowing the empty subarray (so the answer is non-negative).

Input:
    arr: A list of ints

Output:
    The maximum sublist sum

Example:
    >>> max_sublist_sum([4, -5, 2, 1, -1, 3])
    5
"""
