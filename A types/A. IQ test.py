n = int(input())
a = list(map(int, input().split()))
od = 0
ev = 0
for i in range(3):
    if(a[i]%2==0):
        ev += 1
    else:
        od += 1

rem = 0
if(od>ev):
    rem = 1

for i in a:
    if not i%2==rem:
        print(a.index(i)+1)
        break
 