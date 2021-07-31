import math
n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(1,n):
    s += a[i-1]
    print(s)
    if a[i-1]==0:
        continue
    ind = i+(2**int(math.log(n-i,2)))-1
    a[ind]+=a[i-1]
    a[i-1] = 0
