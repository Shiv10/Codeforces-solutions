n = int(input())
arr = list(map(int, input().split()))

m = max(arr)
mi = min(arr)
inm = arr.index(m)
inmi = len(arr) - arr[::-1].index(mi) - 1
c = 0
if(inm<inmi):
    c = inm + (len(arr)-inmi-1)
else:
    c = (inm - 1) + (len(arr)-inmi-1)

print(c)

