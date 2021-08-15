n, m = map(int, input().split())
if m>n:
    print(-1)
    exit()
c = 0
c = n//2
if n%2==1:
    c+=1
if c%m==0:
    print(c)
    exit()
p = c%m
p = m - p
c += p
print(c)