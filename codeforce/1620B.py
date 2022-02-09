for _ in range(int(input())):
    w, h = map(int, input().split())
    h1 = input().split()[1:]
    h1_m = int(h1[-1]) - int(h1[0])
    h2 = input().split()[1:]
    h2_m = int(h2[-1]) - int(h2[0])
    v1 = input().split()[1:]
    v1_m = int(v1[-1]) - int(v1[0])
    v2 = input().split()[1:]
    v2_m = int(v2[-1]) - int(v2[0])
    s1 = max(h1_m, h2_m) * h
    s2 = max(v1_m, v2_m) * w
    ans = max(s1, s2)
    print(ans)
