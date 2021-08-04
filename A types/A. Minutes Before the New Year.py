t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    n = (24-h)*60 - m
    print(n)