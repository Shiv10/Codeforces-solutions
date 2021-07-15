n = int(input())
a = {}
for i in range(n):
    s = input()
    if s not in a.keys():
        print("OK")
        a[s] = 1
    else:
        c = a[s]
        a[s] += 1
        s += str(c)
        print(s)