n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = []
for i in b:
    temp  = 0
    c = [0]
    flag = True
    for j in range(n):
        if a[j]==i and flag:
            c[0] = a[j]
            flag = False
            temp = j
            continue
        c.append(a[j])
    d.append(str(temp+1))
    a = c
print(' '.join(d))
