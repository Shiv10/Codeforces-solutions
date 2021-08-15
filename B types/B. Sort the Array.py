import collections
n = int(input())
start, end = -1, -1
a = list(map(int, input().split()))
b = a[0:]
b.sort()
k = 0
for i in range(n):
    if a[i]!=i:
        start = i
        break

for i in range(n-1,-1, -1):
    if a[i]!=i:
        end = i
        break
if start == -1 or end == -1:
    print("yes")
    print("1 1")
    exit()

print(start,end)

