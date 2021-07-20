import sys

sys.setrecursionlimit(10 ** 6)


def calc(n, d):
    if n in d:
        return d[n]
    if n == 0:
        return 0
    if n < 0:
        return None
    m = None
    for i in p:
        x = calc(n - i, d)
        if x != None:
            x += 1
            if m == None or m < x:
                m = x
    d[n] = m
    return m


n, *p = map(int, input().split())
print(calc(n, {}))