n = int(input())
s = input()
a = list(map(int, input().split()))
f = True
b = [0] * len(a)
i = 0
while(f):
    if b[i] == 1:
        f = False
    b[i] = 1
    if s[i] == ">":
        i+=a[i]
    else:
        i-=a[i]
    if(i>=n or i<0):
        break
        
if f:
    print("FINITE")
else:
    print("INFINITE")
