t = int(input())
while(t>0):
    m, n = map(int, input().split())
    s = m*n
    if(s%2==0):
        s = s//2
    else:
        s = (s+1)//2
    print(s)
    t-=1