n = int(input())
a = list(map(int,input().split()))
s = sum(a)
c = 0
for i in a:
    if (s-i)%2==0:
        c+=1
print(c)