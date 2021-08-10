t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = []
    c = 1
    for i in range(n):
        d.append([a[i],i])

    d = sorted(d, key=lambda x: (x[0]))
    
    for i in range(1,n):
        if d[i-1][1]+1 != d[i][1]:
            c+=1
    if c<=k:
        print("Yes")
        continue
    print("No")
    




