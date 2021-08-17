t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ma = a[0]
    mi = a[0]
    ima = 0
    imi = 0
    c = 0
    for i in range(n):
        if a[i]<mi:
            mi = a[i]
            imi = i
        
        if a[i]>ma:
            ma = a[i]
            ima = i

    c = min(max(imi,ima)+1, n-1-min(imi, ima)+1, n-1- imi + ima + 2, n-1-ima+imi+2)
    
    print(c)



