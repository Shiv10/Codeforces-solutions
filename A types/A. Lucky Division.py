n = int(input())
f = False
for i in range(1,n+1):
    if(f):
        break
    if n%i==0:
        s = str(i)
        if("1" in s or "2" in s or "3" in s or "5" in s or "6" in s or "8" in s or "9" in s):
            continue
        f = True

if(f):
    print("YES")
    exit()

print("NO")