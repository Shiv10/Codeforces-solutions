n = int(input())
a = list(map(int, input().split()))
d = [0]*(max(a)+1)
dp = d[0:]
for i in a:
    d[i]+=1

dp[0] = 0
dp[1] = d[1]

for i in range(2,len(d)):
    dp[i] = max(dp[i-1], i*d[i]+dp[i-2])

print(dp[-1])
