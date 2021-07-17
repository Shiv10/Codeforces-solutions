a, b = map(int, input().split())
m = min(a,b)
ma = max(a,b)
n = ma-m
if n>=2:
    n = n//2
else:
    n = 0
print(str(m)+" "+str(n))