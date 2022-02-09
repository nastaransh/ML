def find(num1, num2, num3):
    guess = [num1, num2, num3]
    ans = 0
    if 1 not in guess:
        ans = 1
    if 2 not in guess:
        ans = 2
    if 3 not in guess:
        ans = 3
    if 4 not in guess:
        ans = 4
    return ans
