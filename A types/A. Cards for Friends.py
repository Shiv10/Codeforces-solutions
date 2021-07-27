t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())
    c = 1
    while(w%2==0 or h%2==0):
        c *= 2
        if (w%2==0):
            w=w//2
        else:
            h=h//2
    if c>=n:
        print("YES")
    else:
        print("NO")