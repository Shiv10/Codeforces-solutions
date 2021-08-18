def calc(a,x,d):
    if d.get(a, -1)!=-1:
        return d
    
    c = 1
    t = a
    while a%x ==0:
        c+=1
        a//=x
    d[t] = c
    return d
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int,input().split()))
    d = {}
    c = 0
    ind = 0
    temp = 0
    m = 10**9
    flag = False
    for i in range(n):
        d = calc(a[i], x, d)
        if d[a[i]] < m:
            m = d[a[i]]
            ind = i
    
    for i in range(n):
        if i < ind:
            c += a[i]*(m+1)
        else:
            c += a[i] * m
    print(c)
