import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = math.ceil(k/(n-1))
    a = n*(s-1)
    b = k - ((n-1)*(s-1))
    print(a+b)