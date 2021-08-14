n = int(input())
d = {}
m = 0
w = ""
for i in range(n):
    s = input()
    if s in d.keys():
        d[s]+=1
    else:
        d[s] = 1
    
    if d[s]>m:
        m = d[s]
        w = s
print(w)