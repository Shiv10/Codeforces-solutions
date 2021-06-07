a = input()[::-1]
s = input()[::-1]
c = 0
while (a[c]==s[c]):
    c+=1
    if c==len(a) or c==len(s):
        break

i = len(a) - c + len(s) - c
print(i)