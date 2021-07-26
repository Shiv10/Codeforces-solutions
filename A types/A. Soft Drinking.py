n, k, l, c, d, p, nl, np = map(int, input().split())
nl = (k*l)//nl
c = (c*d)//n
m = p//np
m = min(nl, c, m)//n
print(m)