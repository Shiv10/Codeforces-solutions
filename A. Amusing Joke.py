s1 = list(input())
s2 = list(input())
s = list(input())
if not ((len(s1)+len(s2)) == (len(s))):
    print("NO")
    exit()
for i in s1:
    if i in s:
        id = s.index(i)
        s[id] = ''
    else:
        print("NO")
        exit()

for i in s2:
    if i in s:
        id = s.index(i)
        s[id] = ''
    else:
        print("NO")
        exit()

print("YES")
