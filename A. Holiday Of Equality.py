n = int(input())
a = list(map(int, input().split()))
m = max(a)
c = 0
for i in a:
    c+=m-i
print(c)