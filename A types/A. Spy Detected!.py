t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0]!=a[1] and a[1]==a[2]:
        print(1)
    if a[n-1]!=a[n-2] and a[n-2]==a[n-3]:
        print(n)
    for i in range(1,n-1):
        if a[i]!=a[i+1] and a[i]!=a[i-1]:
            print(i+1)
            break

    
