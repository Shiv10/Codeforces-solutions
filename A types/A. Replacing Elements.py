t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if a[n-1]<=d:
        print("YES")
        continue
    if a[1]+a[0]<=d:
        print("YES")
        continue
    print("NO")