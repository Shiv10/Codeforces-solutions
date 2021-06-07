n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    if(a<=b):
        print(b)
        continue
    if(c<=d):
        print(-1)
        continue
    e = a-b
    t = c-d
    if(e%t==0):
        t = e//t
    else:
        t = (e//t)+1
    print(b+(c*t))