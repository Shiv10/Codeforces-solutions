num = int(input())
a = list(sorted(list(map(int, input().split()))))
t = int(input())
for _ in range(t):
    n = int(input())
    high = num
    low = 0
    if (n >= a[high-1]):
        print(num)
        continue
    if(n<a[low]):
        print(0)
        continue
    while(high>low):
        mid = (high+low)//2
        if n<a[mid]:
            high=mid
        else:
            low = mid+1

    print(low)