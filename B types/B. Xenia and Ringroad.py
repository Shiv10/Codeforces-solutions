n, m = map(int, input().split())
a = list(map(int, input().split()))

c = a[0] - 1
for i in range(1,m):
    if (a[i-1]<=a[i]):
        c+=a[i]-a[i-1]
    else:
        c += n - a[i-1] + a[i]
print(c)