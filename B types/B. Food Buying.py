t = int(input())
for _ in range(t):
    n = int(input())
    if n < 10:
        print(n)
        continue
    if n%9==0:
        r = n//9
        d = n + (r-1)
        print(d)
        continue
    r = n//9
    d = r*10
    n = n - (r*9)
    print(d+n)
