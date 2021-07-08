s = input().lower()
a = ['h', 'e', 'l', 'l', 'o']
c = 0
for i in s:
    if i == a[c]:
        a[c] = ''
        c+=1
    if c==len(a):
        break
w = ""
w = w.join(a)
if(w==""):
    print("YES")
    exit()
print("NO")
