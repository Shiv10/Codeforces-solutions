t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    m = min(x,y)
    s = 0
    s += (a*(x-m))+(a*(y-m))
    s += b*m
    t = (a*(x+y))
    print(min(s,t)) 