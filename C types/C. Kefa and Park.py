import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
visited = [False]*n
count = 0
for _ in range(n-1):
    a, b = map(int, input().split())
    if d.get(a, -1) == -1:
        d[a] = [b]
    else:
        d[a].append(b)
    
    if d.get(b, -1)== -1:
        d[b] = [a]
    else:
        d[b].append(a)


def dfs(n, c=0):
    global count
    visited[n-1]=True
    if arr[n-1]==1:
        c+=1
    else:
        c = 0

    if c>m:
        return

    if len(d[n]) ==1 and visited[d[n][0]-1]:
        if c<=m and n!=1:
            count += 1
        return


    for i in d[n]:
        if not visited[i-1]:
            dfs(i,c)

dfs(1)
print(count)
