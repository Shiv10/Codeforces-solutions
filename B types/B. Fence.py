n, k = map(int, input().split())
a = list(map(int, input().split()))
c = sum(a[:k])
s = c
res = 0
for i in range(1,n-k+1):
    s = s - a[i-1] + a[i+k-1]
    if s<c:
        c = s
        res = i

print(res+1)
