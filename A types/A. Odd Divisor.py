t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==1:
        print("YES")
        continue
    if n%2==0:
        n = n//2
        f = True
        while (n>1):
            if n%2==1:
                f = False
                print("YES")
                break
            n=n//2
        if f:
            print("NO")
            