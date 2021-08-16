n = int(input())
a = list(map(int, input().split()))
m = a[0]
d = {}
mi = a[0]
for i in range(n):
    if a[i]>m:
        m = a[i]
    if a[i]<mi:
        mi = a[i]
    if d.get(a[i], 0) == 0:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

dif = m - mi
t = d[m]*d[mi]
if dif == 0:
    t = (d[m]*(d[m]-1))//2
print(dif, t)
