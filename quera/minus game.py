def game(number):
    number = str(number)
    big = int(max(number[0], number[1]))
    small = int(min(number[0], number[1]))
    ans = big - small
    return ans
