s = input()
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = 0
a = 0
b = 0
for i in s:
    b = arr.index(i)
    n = abs(a-b)
    m = 26-max(a,b)+min(a,b)
    c += min(n,m)
    a = b

print(c)