def canConstruct(s, a, d = {}):
    if s in d.keys():
        return d[s]
    if s == "":
        return 1
    c = 0
    for i in a:
        if i == s[:len(i)]:
            res = canConstruct(s[len(i):], a, d)
            c+=res
    d[s] = c
    return c

s = input()
a = input().split()
print(canConstruct(s, a))