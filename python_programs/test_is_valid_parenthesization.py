from is_valid_parenthesization import is_valid_parenthesization

# Test cases
assert is_valid_parenthesization('((()()))()') == True, "Test case 1 failed"
assert is_valid_parenthesization(')()(') == False, "Test case 2 failed"
assert is_valid_parenthesization('(') == False, "Test case 3 failed"
assert is_valid_parenthesization('') == True, "Test case 4 failed"
assert is_valid_parenthesization('()') == True, "Test case 5 failed"
assert is_valid_parenthesization('(()') == False, "Test case 6 failed"

print("All test cases passed!")
