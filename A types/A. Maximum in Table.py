n = int(input())
a = []
b = [1]*n
a.append(b)
for i in range(1,n):
    b = [1]
    for j in range(1,n):
        b.append(b[j-1]+a[i-1][j])
    a.append(b)

print(a[n-1][n-1])
