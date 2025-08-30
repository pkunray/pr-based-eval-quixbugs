def lis(arr):
    if not arr:
        return 0

    ends = [0] * len(arr)
    longest = 1

    for i in range(1, len(arr)):
        if arr[i] < arr[ends[0]]:
            ends[0] = i
        elif arr[i] > arr[ends[longest - 1]]:
            ends[longest] = i
            longest += 1
        else:
            left, right = 0, longest - 1
            while left < right:
                mid = (left + right) // 2
                if arr[ends[mid]] < arr[i]:
                    left = mid + 1
                else:
                    right = mid
            ends[left] = i

    return longest


"""
Longest Increasing Subsequence

Input:
    arr: A sequence of ints

Precondition:
    The ints in arr are unique

Output:
    The length of the longest monotonically increasing subsequence of arr

Example:
    >>> lis([4, 1, 5, 3, 7, 6, 2])
    3
"""
