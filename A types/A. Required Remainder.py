t = int(input())
for i in range(t):
    x, y, n = map(int, input().split())

    n1 = n//x
    n1 = n1*x
    while(True):
        if(n1+y<=n):
            print(n1+y)
            break
        n1-=x

        