n = int(input())
for _ in range(n):
    t = input()
    a = []
    for i in range(len(t)):
        if not t[i] == "0":
            b = t[i] + ("0"*(len(t)-i-1))
            a.append(b)
    print(len(a))
    s = " ".join(a)
    print(s)
