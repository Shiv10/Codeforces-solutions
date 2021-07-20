n, m = map(int, input().split())
c = n
while(n>=m):
    c+= n//m
    n = (n//m) + (n%m)
print(c)