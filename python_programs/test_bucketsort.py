def test_bucketsort():
    # Test case 1: Empty list
    assert bucketsort([], 0) == []

    # Test case 2: List with one element
    assert bucketsort([0], 1) == [0]

    # Test case 3: List with multiple elements
    assert bucketsort([3, 1, 2, 1], 4) == [1, 1, 2, 3]

    # Test case 4: List where all elements are the same
    assert bucketsort([2, 2, 2], 3) == [2, 2, 2]

    print("All test cases passed!")

# Run the test function
test_bucketsort()
