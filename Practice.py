a = list(map(int, input().split()))
a.sort()
c = 1
for i in range(len(a)):
    if a[i] != c and a[i]>c:
        print(c)
        exit()
    if a[i]==c:
        c+=1
print(c)