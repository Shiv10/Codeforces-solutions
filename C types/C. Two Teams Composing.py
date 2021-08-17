t = int(input())
for _ in range(t):    
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    m = 0
    mn = 0
    c = 0
    for i in range(n):
        if d.get(a[i], 0) == 0:
            c+=1
            d[a[i]] = 1
        else:
            d[a[i]] += 1
        if m<d[a[i]]:
            m = d[a[i]]
            mn = a[i]

    p = max(min(c-1, d[mn]), min(c, d[mn]-1))
    print(p)
 