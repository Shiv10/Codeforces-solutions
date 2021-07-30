t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    m = max(a)
    if not a.count(m)>=2:
        print("NO")
        continue
    print("YES")
    if a[0] == a[1] == a[2]:
        print(str(a[0])+" "+str(a[0])+" "+str(a[0]))
    else:
        c = list(filter(lambda x: x!=m, a))
        print(str(m)+" "+str(c[0])+" 1")