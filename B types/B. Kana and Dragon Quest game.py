t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    while (m>0):
        if n//2 + 10 <n:
            n = n//2+10
            m-=1
        else:
            break
    if n<=10*k:
        print("YES")
        continue
    print("NO")