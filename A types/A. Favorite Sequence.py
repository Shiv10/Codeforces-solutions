t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    c = 0
    for i in range(n):
        if i%2==0 and i>=2:
            c+=1
        if i%2==0:
            b[i] = str(a[c])
        else:
            b[i] = str(a[n-c-1])
    print(' '.join(b))