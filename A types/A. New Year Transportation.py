n, t = map(int,input().split())
a = list(map(int, input().split()))
b = [0] *(len(a)+1)
b[1:] = a[0:]
c = 1
while(c<t):
    c+=b[c]
if(c==t):
    print("YES")
    exit()
print("NO")