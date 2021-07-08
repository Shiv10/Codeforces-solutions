n, m, a = map(int, input().split())
ans = ((m+a-1)//a) * ((n+a-1)//a)
print(ans)