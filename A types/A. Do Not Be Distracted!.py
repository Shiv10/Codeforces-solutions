t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = []
    f = True
    for i in s:
        if i in a:
            continue
        c = s.count(i)
        w = i*c
        if w not in s:
            f = False
            break
        a.append(i)
    if f:
        print("YES")
    else:
        print("NO")