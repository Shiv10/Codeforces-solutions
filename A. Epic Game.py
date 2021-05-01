a, b, n = map(int, input().split())
c = 0
def compute_hcf(x, y):
    hcf = 1
    for i in range(1, min(x,y)+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

while(True):
    if(c%2==0):
        gcd = compute_hcf(a,n)
        if(n<gcd):
            print(1)
            break
        n-=gcd
    else:
        gcd = compute_hcf(b,n)
        if(n<gcd):
            print(0)
            break
        n-=gcd
    c+=1


