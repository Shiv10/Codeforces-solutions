t = int(input())
for _ in range(t):

    n, k = map(int, input().split())
    if n<k:
        print(k-n)
        continue
    if (n%2==k%2):
        print('0')
        continue
    
    print('1')
