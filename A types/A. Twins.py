n = int(input())
a = list(map(int, input().split()))
s = sum(a)
s = s//2
a = list(sorted(a, reverse=True))
c = 0
n = 0
for i in a:
    if(n>s):
        break
    n += i
    c += 1

print(c)