for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    if (a == b and c % 2 == 0) or (b == c and a % 2 == 0) or (a + b == c):
        print('YES')
    else:
        print('NO')
