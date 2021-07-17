n = int(input())
a = {}
for i in range(n):
    s,t = map(int, input().split())
    a[s] = t

n = int(input())
b = {}
for i in range(n):
    s,t = map(int, input().split())
    b[s] = t

for i in a.keys():
    if i in b.keys():
        if a[i]>b[i]:
            b[i] = 0
        else:
            a[i] = 0

c = 0
for i in a.keys():
    c+=a[i]
for i in b.keys():
    c+=b[i]
print(c)