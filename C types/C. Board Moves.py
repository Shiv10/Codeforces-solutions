t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    p = n//2
    a = n-2
    while(p>0):
        c += 4*p
        c += 4*a*p
        p = a//2
        a -= 2
    print(c)
