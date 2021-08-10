import math
n,m = map(int, input().split())
t = 7-max(m,n)
x = math.gcd(t,6)
print(str(t//x)+"/"+str(6//x))
