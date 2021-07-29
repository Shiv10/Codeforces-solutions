n = int(input())
od = 0
ev = 0
a = list(map(int, input().split()))
i = 0
while(len(a)>0):
    m = max(a[0], a[len(a)-1])
    if i%2==0:
        ev+=m
    else:
        od += m
    if a[0]==m:
        del a[0]
    else:
        del a[len(a)-1]
    i+=1
print(str(ev)+" "+str(od))