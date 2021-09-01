n = int(input())
s = int(input())
global l
l = list(map(int, input().split()))
global d
global visited
visited = [False]*n
d = {}
m = (10**9)*-1


for i in range(n-1):
    a, b = map(int, input().split())
    if(d.get(a,-1)==-1):
        d[a] = [b]
    else:
        d[a].append(b)

def dfs(root, product):
    global m
    visited[root-1] = True
    if root!=s:
        product = product*l[root-1]
    if d.get(root, -1)==-1:
        if product>m:
            m = product
        return
    for i in d[root]:
        if visited[i-1]:
            continue
        else:
            dfs(i, product)
dfs(s, l[s-1])
print(m)