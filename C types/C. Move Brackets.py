t = int(input())
for _ in range(t):
    n = int(input())
    s = [i for i in input()]
    c = 0
    for i in range(n):
        if s[i] == "(":
            if ")" in s[i:]:
                a = s[i:].index(")")
                s[a+i] = "-"
            else:
                c+=1
    print(c)