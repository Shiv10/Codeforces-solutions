t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    s = []
    for i in a:
        if i not in s:
            s.append(i)
    w = " ".join(s)
    print(w)