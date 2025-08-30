def kth(arr, k):
    if not arr:
        raise ValueError("Array is empty")

    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    above = [x for x in arr if x > pivot]

    num_below = len(below)
    num_below_or_equal = num_below + len(equal)

    if k < num_below:
        return kth(below, k)
    elif k < num_below_or_equal:
        return pivot
    else:
        return kth(above, k - num_below_or_equal)


"""
QuickSelect

Input:
    arr: A list of ints
    k: An int

Precondition:
    0 <= k < len(arr)

Output:
    The kth-lowest element of arr (0-based)
"""
