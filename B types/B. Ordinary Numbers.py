t = int(input())
for _ in range(t):
    n = int(input())
    c=0
    s = str(n)
    if n>=10:
        c+=9
    else:
        print(n)
        continue
    
    a = int(s[0])
    b = len(s[1:])
    c += 9*(b-1)
    c += a-1
    d = int(str(a)*len(s))
    if d<=n:
        c+=1
    print(c)

    