s = input()
c = 0
a = [0]
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
        
    a.append(c)
m = int(input())
for i in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(a[r] - a[l])