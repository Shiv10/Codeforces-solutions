n = int(input())
a = list(map(int, input().split()))
ma = max(a)
mi = min(a)
for i in range(n):
    elem_max = max(abs(a[i]-ma),abs(a[i]-mi))
    if i == 0:
        elem_min = abs(a[i]-a[i+1])
        print(elem_min, elem_max)
        continue
    if i == n-1:
        elem_min = abs(a[i]-a[i-1])
        print(elem_min, elem_max)
        continue
    elem_min = min(abs(a[i]-a[i-1]), abs(a[i]-a[i+1]))
    print(elem_min, elem_max)

    