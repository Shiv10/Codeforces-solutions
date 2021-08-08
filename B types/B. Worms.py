n = int(input())
a = list(map(int, input().split()))
d = {}
s = a[0]
for i in range(1,a[0]+1):
    d[i] = 1

for i in range(1,n):
    for j in range(s+1,s+a[i]+1):
        d[j] = i+1
    s+=a[i]

c = int(input())
m = list(map(int, input().split()))
for i in m:
    print(d[i])

