t = int(input())
for _ in range(t):
    n, s, toys = map(int, input().split())
    if n==s and n==toys:
        print(1)
        continue
    if n==s:
        print(s-toys+1)
        continue
    if n==toys:
        print(toys-s+1)
        continue
    mi = min(s, toys)
    ad = n - mi
    print(ad+1)
    