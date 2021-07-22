t = int(input())
for _ in range(t):
    n = int(input())
    s1 = 0
    s2 = 0
    for i in range(1,n//2):
        s1 += 2**i
    s1+=2**n
    for i in range(n//2, n):
        s2 += 2**i
    print(abs(s1-s2))