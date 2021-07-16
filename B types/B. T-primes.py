import math
ma =  10**6
f = [True]*ma
f[0] = f[1] = False
for i in range(2, ma):
    if f[i]:
        for j in range(i*i, ma, i):
            f[j] = False
    
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i==1:
        print("NO")
        continue
    if i==4:
        print("YES")
        continue
    if i%2==0:
        print("NO")
        continue
    m = math.sqrt(i)
    if m == int(m):
        if f[int(m)]:
            print("YES")
        else:
            print("NO")
        continue
    print("NO")