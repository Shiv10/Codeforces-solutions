t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n%2==k%2 and k**2<=n:
        print("YES")
        continue
    print("NO")