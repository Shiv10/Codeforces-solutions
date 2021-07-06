n = int(input())
for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    f = False
    for i in range(t):
        if not (a[i]==m):
            continue
    
        if i==0:
            if a[i+1]<m:
                print(i+1)
                f = True
                break
        
        if i>0 and i<t-1:
            if a[i+1]<m or a[i-1]<m:
                print(i+1)
                f = True
                break

        if i == t-1:
            if a[i-1]<m:
                print(i+1)
                f = True
                break
    
    if not f:
        print(-1)

