def mergeSort(a, s):
    if len(a)<2:
        return
    
    mid = len(a)//2
    l = a[:mid]
    r = a[mid:]
    l1 = s[:mid]
    r1 = s[mid:]

    mergeSort(l,l1)
    mergeSort(r,r1)
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i]<r[j]:
            a[k] = l[i]
            s[k] = l1[i]
            i+=1
        else:
            a[k] = r[j]
            s[k] = r1[j]
            j+=1
        k+=1
    
    while i<len(l):
        a[k]=l[i]
        s[k]=l1[i]
        i+=1
        k+=1
    
    while j<len(r):
        a[k] = r[j]
        s[k] = r1[j]
        j+=1
        k+=1

n = int(input())
a = []
s = []
for i in range(n):
    b, c = (map(int, input().split()))
    a.append(b)
    s.append(c)

mergeSort(a, s)
for i in range(n-1):
    if s[i] > s[i+1] and a[i] < a[i+1]:
        print("Happy Alex")
        exit()
print("Poor Alex")
