for _ in range(int(input())):
    a, b, c = map(int, input().split())
    mult_a = int((2 * b - c) / a)
    mult_b = int((a + c) / (2 * b))
    mult_c = int((2 * b - a) / c)
    if (mult_a > 0 and mult_a * a - b == b - c) or (
            mult_b > 0 and a - mult_b * b == mult_b *b -c) or (mult_c > 0 and a - b == b - mult_c*c):
        print('YES')
    else:
        print('NO')