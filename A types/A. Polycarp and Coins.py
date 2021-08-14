t = int(input())
for _ in range(t):
    n = int(input())
    c1, c2 = 0, 0
    c2 = n//2
    if n%2!=0:
        c1 = 1
    
    m = c2//3
    c2 = c2 - m
    c1 += 2*m
    if c2-c1>1:
        c2 -= 1
        c1 += 2
    print(c1, c2)
