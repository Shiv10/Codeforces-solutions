t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tw = arr.count(2)
    on = arr.count(1)
    if(tw%2==0 and on%2==0):
        print("YES")
        continue
    if(on%2==0 and on!=0):
        print("YES")
        continue
    print("NO")