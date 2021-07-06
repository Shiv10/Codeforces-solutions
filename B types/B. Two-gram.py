n = int(input())
s = input()
d = {}
for i in range(1,n):
    w = s[i-1]+s[i]
    if w in d.keys():
        d[w]+=1
    else:
        d[w] = 1

max_key = max(d, key=d.get)

print(max_key)