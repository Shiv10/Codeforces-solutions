t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    n = max(2*min(a,b), max(a,b))
    print(n*n)