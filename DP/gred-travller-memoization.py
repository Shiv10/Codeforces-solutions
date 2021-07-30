def gridtraveller(n,m, d = {}):
    if (n,m) in d.keys():
        return d[(n,m)]
    if (m, n) in d.keys():
        return d[(m,n)]
    if n==0 or m == 0:
        return 0
    if n==1 and m ==1:
        return 1
    
    d[(n,m)] = gridtraveller(n-1,m)+gridtraveller(n,m-1)
    return d[(n,m)]
    
n = int(input())
m = int(input())
print(gridtraveller(n,m))