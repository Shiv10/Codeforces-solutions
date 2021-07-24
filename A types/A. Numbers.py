from math import gcd
n = int(input())
s = 0
for i in range(2,n):
    t = n
    while t>0:
        s += t%i
        t=t//i
t = n-2
d = gcd(s, t)
s = s//d
t = t//d
print(str(s)+"/"+str(t))
