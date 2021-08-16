t, n = map(int, input().split())
a = list(map(int, input().split()))
d = {t: 1}
b = [a[t-1]]
for i in range(t-2, -1, -1):
    if a[i] in b:
        d[i+1] = d[i+2]
    else:
        d[i+1] = d[i+2]+1
        b.append(a[i])


for _ in range(n):
    c = int(input())
    print(d[c])