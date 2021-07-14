s, n = map(int, input().split())
d = {}
for i in range(n):
    x, p = map(int, input().split())
    if x in d.keys():
        d[x] += p
        continue
    d[x] = p

flag = False
for i in sorted(d.keys()):
    if (i>=s):
        flag = True
        break
    s += d[i]
if not flag:
    print("YES")
    exit()
print("NO")