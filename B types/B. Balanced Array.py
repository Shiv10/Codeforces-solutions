t= int(input())
for _ in range(t):
    n = int(input())
    if not (n//2)%2==0:
        print("NO")
        continue
    print("YES")
    a = [0]*n
    se = 0
    so = 0
    for i in range(n//2):
        a[i] = str(i*2+2)
        se += int(a[i])
        a[i+n//2] = str(i*2+1)
        so += int(a[i+n//2])
    a[n-1] = str(se - (so-int(a[n-1])))
    s = " ".join(a)
    print(s)