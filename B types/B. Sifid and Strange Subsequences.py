t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if len(a)<2:
        print(len(a))
        continue
    
    if a[len(a)-1]<=0:
        print(len(a))
        continue
    
    p = 0
    diff = a[1]-a[0]
    for i in range(1,n):
        if a[i]>0:
            p=i
            break

        d = a[i+1] - a[i]
        if d<diff:
            diff = d
    
    if a[p]<=diff:
        print(p+1)
    else:
        print(p)

