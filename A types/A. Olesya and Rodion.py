n, t = map(int, input().split())
n = (10**n)
f = False
for i in range(n-1,n-11, -1):
    if i<1:
        f = True
        break
    if i%t==0:
        print(i)
        break

if f:
    print(-1)