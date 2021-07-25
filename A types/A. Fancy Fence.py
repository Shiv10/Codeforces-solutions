t = int(input())
for _ in range(t):
    d = int(input())
    n = 360/(180-d)
    if n==int(n):
        print('YES')
        continue
    print("NO")