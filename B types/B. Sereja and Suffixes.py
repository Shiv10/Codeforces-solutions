t, n = map(int, input().split())
a = list(map(int, input().split()))
d = {}
b = [0] * len(a) 
s = 0
for i in range(t-1, -1, -1):
    if d.get(a[i], 0) == 0:
        d[a[i]] = 1
        s += 1
    b[i] = s

for _ in range(n):
    c = int(input())
    print(b[c-1])