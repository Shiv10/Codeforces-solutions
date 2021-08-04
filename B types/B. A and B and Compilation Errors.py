n = int(input())
a = list(sorted(map(int, input().split())))
b = list(sorted(map(int, input().split())))
c = list(sorted(map(int, input().split())))
f = False
for i in range(len(b)):
    if a[i]!=b[i]:
        f = True
        print(a[i])
        break

if not f:
    print(a[len(a)-1])

f = False
for i in range(len(c)):
    if c[i]!=b[i]:
        f = True
        print(b[i])
        break

if not f:
    print(b[len(b)-1])