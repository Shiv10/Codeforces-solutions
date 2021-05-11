n = int(input())
a = list(map(int, input().split()))
c1 = 0
c2 = 0
c3 = 0

for i in a:
    if i == 1:
        c1+=1

    if i == 2:
        c2+=1

    if i == 3:
        c3+=1

n = min(c1,c2,c3)   
print(n) 
if(n>0):
    for i in range(n):
        print(str(a.index(1)+1)+' '+str(a.index(2)+1)+' '+str(a.index(3)+1))
        a[a.index(1)] = -1
        a[a.index(2)] = -1
        a[a.index(3)] = -1
