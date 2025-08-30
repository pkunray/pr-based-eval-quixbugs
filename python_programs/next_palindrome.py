def next_palindrome(digit_list):
    n = len(digit_list)
    if all(x == 9 for x in digit_list):
        return [1] + [0] * (n - 1) + [1]

    # Step 1: Mirror the left half onto the right half
    left_half = digit_list[:(n + 1) // 2]
    if n % 2 == 0:
        candidate = left_half + left_half[::-1]
    else:
        candidate = left_half + left_half[-2::-1]

    # Step 2: Check if the candidate is greater than the original
    if candidate > digit_list:
        return candidate

    # Step 3: Increment the middle digit(s) and mirror again
    i = (n - 1) // 2
    while i >= 0:
        if digit_list[i] < 9:
            digit_list[i] += 1
            break
        digit_list[i] = 0
        i -= 1

    left_half = digit_list[:(n + 1) // 2]
    if n % 2 == 0:
        return left_half + left_half[::-1]
    else:
        return left_half + left_half[-2::-1]
