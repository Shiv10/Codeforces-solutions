n = int(input())
a = list(map(int, input().split()))

b = [0]*len(a)
for i in a:
    b[i-1] = a.index(i)+1

for i in b:
    print(i, end=" ")