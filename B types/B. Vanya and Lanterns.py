n, l = map(int, input().split())

a = list(sorted(list(map(int, input().split()))))
diff = max(l - a[len(a)-1], a[0]-0)
d = 0
for i in range(n-1):
    if a[i+1] - a[i] > d:
        d = a[i+1] - a[i]

if(d/2<diff):
    d = diff
else:
    d = d/2

print(d)