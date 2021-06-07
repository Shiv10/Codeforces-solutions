t = int(input())
for i in range(t):
    s = input()
    n = int(s[0])
    c = 0
    c += (10*(n-1))
    n = len(s)
    n = (n*(n+1))//2
    c+=n
    print(c)

