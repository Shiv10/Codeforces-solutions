n = int(input())
a = ['']*n
s = input()
t = 0
c = n-1
while (c>0):
    a[t] = s[c-1]
    a[n-t-1] = s[c]
    c-=2
    t+=1
if n%2==1:
    a[n//2]=s[0]

print(''.join(a))