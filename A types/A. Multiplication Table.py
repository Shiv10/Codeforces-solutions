n, x = map(int, input().split())
k = 1
c = 0
while (k<=n and k<((x//2)+1)):
    if x%k==0 and x//k<=n:
        c+=1
    k+=1
if x<=n:
    c+=1
print(c)
    

