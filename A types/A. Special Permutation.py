t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*n
    a[0] = str(n)
    for i in range(1,n):
        a[i] = str(i)
    print(' '.join(a))