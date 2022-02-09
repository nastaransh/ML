for _ in range(int(input())):
    s = input()
    one_count = s.count('1')
    zero_count = s.count('0')
    if one_count > zero_count:
        print(zero_count)
    if one_count < zero_count:
        print(one_count)
    if one_count == zero_count:
        print(len(s) - one_count - 1)
