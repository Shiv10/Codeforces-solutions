m, n = map(int, input().split())
c = 0
for i in range(m):
    if(i%2==0):
        print("#"*n)
    else:
        if(c%2==0):
            print(("."*(n-1))+"#")
        else:
            print("#"+("."*(n-1)))
        c+=1