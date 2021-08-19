s = input()
a = []
b = []
for i in range(len(s)-1):
    if s[i]=='A' and s[i+1]=='B':
        a.append([i,i+1])
    if s[i]=='B' and s[i+1]=='A':
        b.append([i,i+1])

if len(a)>0 and len(b)>0:
    if ((a[0][1]!=b[len(b)-1][0]) and (b[len(b)-1][1]!=a[0][0])) or ((b[0][1]!=a[len(a)-1][0]) and (a[len(a)-1][1]!=b[0][0])):
        print("YES")
        exit()

print("NO")
