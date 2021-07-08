n = int(input())
s = 0
a = []
for i in range(n):
    b =  list(map(int, input().split()))
    a.append(b)

for i in range(3):
    su = 0
    for j in range(n):
        su += a[j][i]
    if(su==0):
        continue
    s=1
    break

if(s==0):
    print("YES")
    exit()

print("NO")