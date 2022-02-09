for _ in range(int(input())):
    x1, x2, y1, y2 = input().split() + input().split()
    x = int(x1 + '0' * int(x2))
    y = int(y1 + '0' * int(y2))
    diff = x - y
    if diff > 0:
        print('>')
    elif diff < 0:
        print('<')
    else:
        print('=')
