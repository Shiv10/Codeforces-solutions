t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    d = abs(a-b)
    c = 0
    while(not d==0):
        if d>=10:
            c+=d//10
            d%=10
            continue
        if d>=9:
            c+=d//9
            d%=9
            continue
        if d>=8:
            c+=d//8
            d%=8
            continue
        if d>=7:
            c+=d//7
            d%=7
            continue
        if d>=6:
            c+=d//6
            d%=6
            continue
        if d>=5:
            c+=d//5
            d%=5
            continue
        if d>=4:
            c+=d//4
            d%=4
            continue
        if d>=3:
            c+=d//3
            d%=3
            continue
        if d>=2:
            c+=d//2
            d%=2
            continue
        if d>=1:
            c+=d//1
            d%=1
            continue

    print(c)