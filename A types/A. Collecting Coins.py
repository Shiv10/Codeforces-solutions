t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    m = max(a,b,c)
    s = (3*m) - (a+b+c)
    n = n-s
    if n<0:
        print("NO")
        continue
    if n%3==0:
        print("YES")
        continue
    print("NO")