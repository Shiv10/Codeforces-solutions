t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    co = 0
    ce = 0
    for j in arr:
        s+=j
        if(j%2==0):
            ce+=1
        else:
            co+=1
    
    if(s%2!=0):
        print("YES")
        continue
    
    if(co>0 and ce>0):
        print("YES")
        continue
    print("NO")
