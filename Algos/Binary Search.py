def binarySearch(a, n):
    low = 0
    high = len(a)-1
    mid = 0
    while low<=high:
        mid = (high+low)//2
        if a[mid]<n:
            low = mid+1
        elif a[mid]>n:
            high = mid-1
        else:
            return mid+1
    return low+1