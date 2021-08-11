t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    k = a[0]
    c = 0
    if a[0]>=0:
        c=1

    for i in range(n):
        if c==1:
            if a[i]<0:
                s += k
                k = a[i]
                c = 0
            else:
                if a[i]>k:
                    k = a[i]
        else:
            if a[i]>=0:
                s += k
                k = a[i]
                c = 1
            else:
                if a[i]>k:
                    k = a[i]

    print(s+k)
