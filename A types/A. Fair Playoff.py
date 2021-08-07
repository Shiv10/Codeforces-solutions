t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    b = list(sorted(a))
    if (b[3] in a[:2] and b[2] in a[2:]) or (b[3] in a[2:] and b[2] in a[:2]):
        print("YES")
        continue
    print("NO")