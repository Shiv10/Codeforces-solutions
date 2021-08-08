s = input()
d = [0]*len(s)
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        d[i]=1
        continue
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    c = sum(d[a:b])
    print(c)