t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int,input().split()))
    i = 0
    c = 0
    while (True):
        if a[i]%x!=0:
            break
        c+=a[i]
        s = a[i]//x
        a = a[0:]+([s]*x)
        i+=1

    while(i<len(a)):
        c+=a[i]
        i+=1
    print(c)
